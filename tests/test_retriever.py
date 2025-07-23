from app.vector_store import load_vector_store

def test_vector_store_loading():
    retriever = load_vector_store()
    docs = retriever.similarity_search("day care surgery")
    assert isinstance(docs, list)
    assert len(docs) > 0