from app.chains import process_insurance_query

def test_end_to_end_query():
    query = "Is day care surgery covered?"
    result = process_insurance_query(query)
    assert "decision" in result
    assert "matched_clauses" in result
    assert "confidence_score" in result