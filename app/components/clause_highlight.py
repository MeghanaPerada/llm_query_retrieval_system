def highlight_clauses(text: str, clauses: list[str]) -> str:
    """Highlights clauses in text with <mark> tags for Streamlit HTML rendering."""
    for clause in clauses:
        text = text.replace(clause, f"<mark>{clause}</mark>")
    return text