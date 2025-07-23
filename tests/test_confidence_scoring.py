from app.chains import process_insurance_query

def test_confidence_score_range():
    query = "Can I get payout for hospital admission due to an accident?"
    result = process_insurance_query(query)
    assert 0.0 <= result['confidence_score'] <= 1.0, "Confidence score out of range"