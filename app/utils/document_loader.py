from langchain.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tempfile
import os

def load_and_split_document(file):
    # Save uploaded file temporarily
    suffix = file.name.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as tmp_file:
        tmp_file.write(file.read())
        tmp_path = tmp_file.name

    # Select appropriate loader
    if suffix == "pdf":
        loader = PyPDFLoader(tmp_path)
    elif suffix == "docx":
        loader = Docx2txtLoader(tmp_path)
    elif suffix == "txt":
        loader = TextLoader(tmp_path)
    else:
        raise ValueError("Unsupported file type. Please upload PDF, DOCX, or TXT.")

    documents = loader.load()

    # Clean up temp file
    os.remove(tmp_path)

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )
    split_docs = text_splitter.split_documents(documents)

    return split_docs