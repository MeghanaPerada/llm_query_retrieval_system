from app.vector_store import load_and_split_documents, create_faiss_index

if __name__ == "__main__":
    folder_path = "data/"  # Update this if your PDFs are in another folder
    chunks = load_and_split_documents(folder_path)
    create_faiss_index(chunks)
    print("✅ FAISS vector index created and saved.")