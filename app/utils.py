import re
import numpy as np

def extract_entities(query: str):
    return {
        "age": re.findall(r"\d{2}", query),
        "location": re.findall(r"in (\w+)", query),
        "procedure": "surgery" if "surgery" in query else "",
        "policy_duration": re.findall(r"\d+-month", query)
    }

def calculate_confidence(similarity_scores: list):
    if not similarity_scores:
        return 0.0
    return round(float(np.mean(similarity_scores)), 2)