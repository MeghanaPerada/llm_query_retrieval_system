from app.utils.document_loader import load_document_text
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import tempfile

def get_top_k_chunks(file, query: str, k=3):
    # 1. Load and chunk the document
    raw_text = load_document_text(file)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(raw_text)

    documents = [Document(page_content=chunk) for chunk in chunks]

    # 2. Vectorize
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(documents, embeddings)

    # 3. Search top k
    retriever = db.as_retriever(search_kwargs={"k": k})
    docs = retriever.get_relevant_documents(query)
    results = [doc.page_content for doc in docs]
    scores = [1.0 for _ in results]  # Dummy scores for now

    return results, scores