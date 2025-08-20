import streamlit as st
from rag import process_url ,generate_answer

# --- Page config ---
st.set_page_config(page_title="Research Engine", layout="wide")


# --- Custom CSS for Styling ---
def local_css():
    st.markdown("""
        <style>
        /* General App Styling & Font Colors */
        [data-testid="stAppViewContainer"] {
            background-color: #f0f2f6;
            background-image: linear-gradient(to right, #f0f2f6, #e6e9f0);
            color: #333;
            padding-top: 1rem; /* Overall top padding for the app */
        }

        /* Reduce space below the main H1 heading */
        h1 {
            color: #0d47a1;
            margin-bottom: 0.25rem; 
        }

        /* Reduce space above and below H3 subheadings */
        h3 {
            color: #0d47a1;
            margin-top: 0.5rem;
            margin-bottom: 0.5rem;
        }

        /* Main Content Container (Right Side) */
        .main-content {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Input Fields */
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            border-radius: 8px;
            border: 2px solid #ccc;
            padding: 10px;
            transition: all 0.3s ease;
        }
        .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
            border-color: #0d47a1;
            box-shadow: 0 0 5px rgba(13, 71, 161, 0.5);
            outline: none;
        }

        /* Button Styling */
        .stButton>button {
            width: 100%;
            border-radius: 8px;
            background-color: #0d47a1;
            color: white;
            padding: 12px 20px;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s ease, transform 0.2s ease;
            border: none;
        }
        .stButton>button:hover {
            background-color: #1976d2;
            transform: translateY(-2px);
        }
        .stButton>button:active {
            transform: translateY(0);
        }

        /* Messages */
        .stSuccess, .stWarning {
            border-radius: 8px;
        }
        </style>
        """, unsafe_allow_html=True)


# --- Apply custom CSS ---
local_css()

# --- Title and Header ---
st.markdown("<h1 style='text-align: center;'>🔬 Research Engine</h1>", unsafe_allow_html=True)

# --- Layout with columns: left for 'How to Use', a spacer, and right for main content ---
col_left, col_spacer, col_right = st.columns([1, 0.3, 2])

with col_left:
    st.subheader("📖 How to Use")
    st.markdown("""
    Welcome to the **Research Engine**! This tool helps you quickly find information from a few trusted web sources.

    Here's how to use it:

    1.  **Add Trusted URLs:** In the **Add URLs** section, paste up to three URLs from trusted **websites URL** or other documents you want to search. These can be articles, reports, or any web pages with relevant information.
    2.  **Enter Your Query:** In the **Enter Your Query** section, type your specific question. The more precise your query, the better the result.
    3.  **Submit Query:** Click the **Submit Query** button. The engine will then process the content from the provided URLs to find the answer to your question.
    """)

with col_right:



    # --- Add URLs Section ---
    st.subheader("🔗 Add URLs")
    url1 = st.text_input("URL 1", placeholder="Paste first URL here", key="url1")
    url2 = st.text_input("URL 2", placeholder="Paste second URL here", key="url2")
    url3 = st.text_input("URL 3", placeholder="Paste third URL here", key="url3")
    Process_url_button=st.button("process_url")

    placeholder = st.empty()

    if Process_url_button:
        urls=[url for url in [url1,url2,url3] if url!=""]
        if len(urls)==0:
            placeholder.text("⚠️ You must provide at least one URL")

        else:
            for status in process_url(urls):
                placeholder.text(status)





    st.markdown("---")

    # --- Query Box Section ---
    st.subheader("🤔 Enter Your Query")
    query = st.text_area(
        "Ask something about the content:",
        height=50,
        placeholder="Type your question here...",
        key="query_input"
    )

    if st.button("Submit Query"):
        try:
            answer,sources=generate_answer(query)
            st.header("Answer.")
            st.write(answer)
            if sources:
                st.subheader("Sources:")
                st.write(sources)
        except RuntimeError as e:
            placeholder.text("Must process url and then query ")


    st.markdown('</div>', unsafe_allow_html=True)