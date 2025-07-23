from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from app.vector_store import load_faiss_index
from app.utils import extract_entities, calculate_confidence

def process_insurance_query(user_query: str):
    vectorstore = load_faiss_index()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    llm = ChatOpenAI(model="gpt-3.5-turbo")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    result = qa_chain.invoke(user_query)

    # Add structured output
    return {
        "decision": "Approved" if "covered" in result['result'].lower() else "Rejected",
        "justification": result['result'],
        "entities": extract_entities(user_query),
        "confidence": calculate_confidence(result.get("source_documents", []))
    }