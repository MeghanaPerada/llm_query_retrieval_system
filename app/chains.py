import json
from llm_chain import run_llm_chain
from utils.document_loader import load_and_split_document
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def process_insurance_query(query, uploaded_file):
    # Load and split document into chunks
    split_docs = load_and_split_document(uploaded_file)
    texts = [doc.page_content for doc in split_docs]

    # Create FAISS vector store from the uploaded document
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(texts, embedding=embeddings)

    # Retrieve top relevant clauses
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})
    relevant_docs = retriever.get_relevant_documents(query)
    clauses = [doc.page_content for doc in relevant_docs]

    # Dummy entity extraction (you can replace with regex or another chain)
    entities = {"query": query}

    # Run the LLM decision chain
    raw_output = run_llm_chain(entities, clauses)

    # Parse LLM response (JSON)
    try:
        parsed = json.loads(raw_output)
    except json.JSONDecodeError:
        parsed = {
            "decision": "Needs More Info",
            "justification_clauses": [],
            "confidence": 0.3,
            "entities": entities
        }

    return {
        "decision": parsed["decision"],
        "justification": "\n\n".join(parsed["justification_clauses"]),
        "confidence": parsed.get("confidence", 0.5),
        "entities": parsed.get("entities", entities),
    }