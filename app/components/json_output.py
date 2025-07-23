def format_decision_json(decision: str, confidence: float, reasons: list[str], clauses: list[str]) -> dict:
    return {
        "decision": decision,
        "confidence_score": round(confidence, 2),
        "explainability_tree": reasons,
        "matched_clauses": clauses
    }