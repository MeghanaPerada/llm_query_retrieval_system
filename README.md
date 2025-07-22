# LLM Query-Retrieval System

An intelligent, production-ready system to **process vague insurance queries** and retrieve the most relevant policy clauses through semantic search and LLM reasoning.



##  Problem We Solve
Manual insurance claim analysis is slow, inconsistent, and lacks explainability.  
Our system automates this by parsing natural language queries and retrieving decisions with clear justification.



## Solution Overview
1️)Parse user query into structured data (age, surgery, policy duration, etc.)  
2️) Retrieve relevant clauses from documents via **FAISS** & **OpenAI embeddings**  
3️) Use **LLM (GPT-4o)** to reason on the context & output decisions  
4️)Expose results via **Streamlit UI / FastAPI API** with clear explainability.



## Tech Stack
Tech Stack
	•	Python 3.12
	•	Poetry (for dependency management via pyproject.toml)
	•	LangChain
	•	FAISS
	•	OpenAI
	•	Streamlit
	•	FastAPI
	•	Uvicorn
	•	PyMuPDF
	•	Python-dotenv


## Project Structure
llm_query_retrieval_system/
├── app/
│   ├── __init__.py
│   ├── chains.py
│   ├── components/
│   ├── streamlit_app.py
│   ├── utils.py
│   ├── vector_store.py
├── data/
├── models/
├── tests/
├── pyproject.toml
├── poetry.lock
├── .gitignore
├── .env  (local only)
├── README.md

## Installation
git clone https://github.com/yourusername/llm_query_retrieval_system.git
cd llm_query_retrieval_system

## Install dependencies using Poetry
poetry install
poetry shell

## Running the app
For Streamlit app:
streamlit run app/streamlit_app.py

For FastAPI (if applicable):
uvicorn app.api:app --reload

## Project Goals
 	•	Automate complex insurance document queries
	•	Provide LLM-powered reasoning with explainability
	•	Ensure production-readiness via proper dependency and environment management

	
License

MIT License
