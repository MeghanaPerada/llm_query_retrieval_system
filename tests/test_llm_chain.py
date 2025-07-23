from app.chains import build_llm_chain

def test_llm_chain_structure():
    chain = build_llm_chain()
    assert hasattr(chain, "invoke"), "LLM chain missing 'invoke' method"