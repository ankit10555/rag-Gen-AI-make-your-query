from cgitb import reset
from uuid import uuid4
from dotenv import load_dotenv
from pathlib import Path
import shutil
from langchain.chains import RetrievalQAWithSourcesChain
import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_groq import ChatGroq

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import shutil



load_dotenv()
chunk_sizes=1000
collection_name="Research_reader"
vectorstore_dir=Path(__file__).parent/"res"

ef="Alibaba-NLP/gte-base-en-v1.5"
llm=None
vector_store=None
def initialize_components():
    global llm,vector_store

    if llm is None:
        llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.3 ,max_tokens=500)

    if vector_store is None:
        vector_store=Chroma(
            collection_name=collection_name,
            embedding_function=HuggingFaceEmbeddings(
                model_name = ef,
                model_kwargs = {'trust_remote_code': True}
            ),
            persist_directory= str(vectorstore_dir)
        )








def process_url(url):
    """this function scrap data from url and store in a vector db
    :param
    :return
    """
    yield  "Initializing component"
    initialize_components()
    yield "Loading_data"
    loader=WebBaseLoader(url)
    data=loader.load()
    yield "spliting text"
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=chunk_sizes,
        separators=["/n/n","/n","."],
    )
    docs=text_splitter.split_documents(data)
    yield "🔍 Query-ready: documents have been loaded"
    vector_store.add_documents(docs,ids=[str(uuid4()) for i in docs])


def generate_answer(query):
    chain=RetrievalQAWithSourcesChain.from_llm(llm=llm,
                                         retriever=vector_store.as_retriever())
    result=chain.invoke({"question":query},return_only_output=True)
    source = result.get('sources') or result.get('source') or ""
    return result['answer'],source


if __name__=="__main__":

    urls = [
        "https://www.cnbc.com/2024/12/21/how-the-federal-reserves-rate-policy-affects-mortgages.html",
        "https://www.cnbc.com/2024/12/20/why-mortgage-rates-jumped-despite-fed-interest-rate-cut.html"
    ]

    # Process and store documents

    process_url(urls)

    # generate a answer:
    answer,source=generate_answer("30  year mortagate rate")
    print(f"Answer:{answer}")
    print(f"Sources:{source}")





