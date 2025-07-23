import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Global config variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./data/faiss_index")
FASTAPI_HOST = os.getenv("FASTAPI_HOST", "127.0.0.1")
FASTAPI_PORT = int(os.getenv("FASTAPI_PORT", 8000))