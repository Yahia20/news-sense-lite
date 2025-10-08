# app.py
# NewsSense Lite — AI-powered news summarizer and Q&A tool

import os
import streamlit as st
import pickle
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import RetrievalQAWithSourcesChain
from transformers import pipeline

# -----------------------------
# Streamlit app configuration
# -----------------------------
st.set_page_config(page_title="NewsSense Lite 🧭", page_icon="🧭")
st.title("🧭 NewsSense Lite — Smart AI News Reader")
st.markdown("Ask questions about news articles using a lightweight AI pipeline.")

# -----------------------------
# Sidebar: article input
# -----------------------------
st.sidebar.header("📰 Article URLs")
urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]
process_url = st.sidebar.button("🚀 Process Articles")

# Path to save FAISS index
INDEX_FILE = "news_faiss_index.pkl"

# -----------------------------
# Model and pipeline setup
# -----------------------------
MODEL_NAME = os.getenv("NEWS_MODEL_NAME", "google/flan-t5-base")

@st.cache_resource(show_spinner=False)
def load_llm(model_name):
    """Initialize the text-to-text model."""
    text_gen = pipeline(
        "text2text-generation",
        model=model_name,
        device_map="auto",
        max_new_tokens=256,
    )
    return HuggingFacePipeline(pipeline=text_gen)

llm = load_llm(MODEL_NAME)
placeholder = st.empty()

# -----------------------------
# Article processing
# -----------------------------
if process_url:
    valid_urls = [u for u in urls if u.strip()]
    if not valid_urls:
        placeholder.warning("Please provide at least one valid URL.")
    else:
        placeholder.info("📥 Loading and parsing articles...")
        try:
            loader = UnstructuredURLLoader(urls=valid_urls)
            documents = loader.load()
        except Exception as e:
            placeholder.error(f"Error loading URLs: {e}")
            documents = []

        if documents:
            placeholder.info("🧩 Splitting text into smaller chunks...")
            splitter = RecursiveCharacterTextSplitter(
                separators=["\n\n", "\n", ".", "?"],
                chunk_size=800
            )
            chunks = splitter.split_documents(documents)

            placeholder.info("🔢 Generating embeddings...")
            embeddings = HuggingFaceEmbeddings()
            vectorstore = FAISS.from_documents(chunks, embeddings)

            with open(INDEX_FILE, "wb") as f:
                pickle.dump(vectorstore, f)

            placeholder.success("✅ Articles processed and indexed successfully!")
        else:
            placeholder.warning("No readable content found in the provided URLs.")

# -----------------------------
# Question answering
# -----------------------------
question = st.text_input("💭 Ask a question about the articles:")

if question:
    if not os.path.exists(INDEX_FILE):
        st.warning("Please process the articles first.")
    else:
        with open(INDEX_FILE, "rb") as f:
            vectorstore = pickle.load(f)

        chain = RetrievalQAWithSourcesChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever()
        )

        with st.spinner("Generating answer..."):
            result = chain({"question": question}, return_only_outputs=True)

        st.header("🧠 Answer")
        st.write(result.get("answer", "No response generated."))

        sources = result.get("sources", "")
        if sources:
            st.subheader("🔗 Sources")
            for s in sources.split("\n"):
                if s.strip():
                    st.write(s.strip())
