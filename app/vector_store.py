import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.config import OPENAI_API_KEY, VECTOR_DB_PATH  # ✅ Use config

def load_and_split_documents(folder_path):
    all_docs = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder_path, file))
            all_docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(all_docs)

def create_faiss_index(chunks):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)  # ✅ Secure key usage
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(VECTOR_DB_PATH)  # ✅ Use env path
    return vectorstore

def load_faiss_index():
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    return FAISS.load_local(VECTOR_DB_PATH, embeddings)