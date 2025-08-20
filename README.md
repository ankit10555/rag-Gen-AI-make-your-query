# RAG Research AI - Web-based Document Analysis

A Retrieval-Augmented Generation (RAG) application that scrapes web content, stores it in a vector database, and provides intelligent question-answering capabilities using LangChain and Groq LLM.

## 🚀 Features

- **Web Content Scraping**: Automatically extracts content from URLs
- **Vector Database Storage**: Uses ChromaDB for efficient document storage and retrieval
- **Intelligent Q&A**: Leverages Groq's LLaMA model for accurate responses
- **Source Attribution**: Provides sources for generated answers
- **Streamlit Interface**: Optional web interface for easy interaction
- **Embeddings**: Uses HuggingFace embeddings for semantic search

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API key (get it from [Groq Console](https://console.groq.com/))
- Internet connection for web scraping and model downloads

## 🛠️ Installation

### Option 1: Using Conda (Recommended)

```bash
# Clone the repository
git clone https://github.com/ankit10555/Rag-generative-AI-Reseach-AI.git
cd Rag-generative-AI-Reseach-AI

# Create and activate conda environment
conda create -n rag_project python=3.11
conda activate rag_project

# Install dependencies
pip install -r requirements-minimal.txt
```

### Option 2: Using pip

```bash
# Clone the repository
git clone https://github.com/ankit10555/Rag-generative-AI-Reseach-AI.git
cd Rag-generative-AI-Reseach-AI

# Install dependencies
pip install -r requirements-minimal.txt
```

## ⚙️ Configuration

1. **Create environment file**:
```bash
# Create .env file in project root
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
```

2. **Create results directory**:
```bash
mkdir res
```

## 🎯 Usage

### Basic Usage

```python
from main import process_multiple_urls, generate_answer

# URLs to process
urls = [
    "https://www.cnbc.com/2024/12/21/how-the-federal-reserves-rate-policy-affects-mortgages.html",
    "https://www.cnbc.com/2024/12/20/why-mortgage-rates-jumped-despite-fed-interest-rate-cut.html"
]

# Process documents
process_multiple_urls(urls)

# Generate answers
answer, sources = generate_answer("What are the current 30-year mortgage rates?")
print(f"Answer: {answer}")
print(f"Sources: {sources}")
```

### Command Line

```bash
# Run the main script
python main.py
```

### Streamlit Interface

```bash
# Run Streamlit app (create streamlit_app.py first)
streamlit run streamlit_app.py
```

## 📁 Project Structure

```
Rag-generative-AI-Reseach-AI/
├── main.py                 # Main RAG application
├── requirements.txt        # Full dependencies
├── requirements-minimal.txt # Essential dependencies only
├── .env                    # Environment variables (create this)
├── res/                    # Vector database storage (create this)
├── README.md              # This file
└── .gitignore             # Git ignore file
```

## 🔧 Key Components

### Core Functions

- **`initialize_components()`**: Sets up LLM and vector database
- **`process_url(url)`**: Scrapes and processes a single URL
- **`process_multiple_urls(urls)`**: Handles multiple URLs
- **`generate_answer(query)`**: Generates answers using RAG

### Configuration Parameters

```python
chunk_sizes = 1000                           # Document chunk size
collection_name = "Research_reader"          # ChromaDB collection name
embedding_model = "Alibaba-NLP/gte-base-en-v1.5"  # HuggingFace embedding model
```

## 📊 Example Queries

- "What are the current mortgage rates?"
- "How does the Federal Reserve affect mortgage rates?"
- "What factors influence mortgage rate changes?"
- "Compare recent mortgage rate trends"

## 🔍 How It Works

1. **Document Processing**: Web content is scraped using BeautifulSoup
2. **Text Splitting**: Documents are chunked using RecursiveCharacterTextSplitter
3. **Embeddings**: Text chunks are converted to vectors using HuggingFace embeddings
4. **Storage**: Vectors are stored in ChromaDB for efficient retrieval
5. **Retrieval**: Similar documents are found using semantic search
6. **Generation**: Groq's LLaMA model generates answers based on retrieved context

## 🛡️ Environment Variables

Create a `.env` file with the following variables:

```bash
GROQ_API_KEY=your_groq_api_key_here
HUGGINGFACE_API_TOKEN=your_hf_token_here  # Optional, for some models
```

## 📦 Dependencies

### Core Dependencies
- `langchain` - LLM framework
- `langchain-groq` - Groq LLM integration
- `langchain-chroma` - ChromaDB integration
- `chromadb` - Vector database
- `sentence-transformers` - Text embeddings
- `beautifulsoup4` - Web scraping
- `streamlit` - Web interface

### Full dependency list available in `requirements.txt`

## 🚨 Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your Groq API key is correctly set in `.env`
2. **Import Errors**: Install all dependencies using `pip install -r requirements-minimal.txt`
3. **Vector Store Error**: Make sure the `res/` directory exists
4. **Memory Issues**: Reduce `chunk_sizes` or use smaller embedding models

### Debug Mode

Add debugging to your code:

```python
def generate_answer(query):
    print(f"Query: {query}")
    print(f"Vector store type: {type(vector_store)}")
    # ... rest of function
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Groq Console](https://console.groq.com/) - Get your API key
- [LangChain Documentation](https://python.langchain.com/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)

## 📧 Contact

**Ankit** - [GitHub](https://github.com/ankit10555)

Project Link: [https://github.com/ankit10555/Rag-generative-AI-Reseach-AI](https://github.com/ankit10555/Rag-generative-AI-Reseach-AI)

---

⭐ **Star this repository if you found it helpful!**