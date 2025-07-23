from fastapi import FastAPI
from pydantic import BaseModel
from app.chains import process_insurance_query
from app.config import OPENAI_API_KEY  # 🔐 Load to ensure .env is triggered

app = FastAPI()

class QueryInput(BaseModel):
    query: str

@app.get("/")
def health_check():
    return {"message": "LLM Query-Retrieval System API Running ✅"}

@app.post("/query")
def query_endpoint(input: QueryInput):
    return process_insurance_query(input.query)