# app/llm_chain.py

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from config import OPENAI_API_KEY  # ✅ Correct

# ✅ pass key explicitly
llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0.2,
    openai_api_key=OPENAI_API_KEY
)

template = """
You are an insurance policy decision assistant.
Given these extracted details from a user's insurance query:
{entities}

And relevant clauses from the policy document:
{clauses}

Please:
1. Make a decision (Approve / Reject / Needs More Info)
2. Justify your decision using specific clauses.
3. Output in JSON with fields: "decision", "justification_clauses", "confidence", "entities"

Respond only with valid JSON.
"""

prompt = ChatPromptTemplate.from_template(template)

llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    output_key="output"
)

def run_llm_chain(entities: dict, clauses: list[str]) -> dict:
    input_data = {
        "entities": str(entities),
        "clauses": "\n".join(clauses)
    }
    return llm_chain.run(input_data)