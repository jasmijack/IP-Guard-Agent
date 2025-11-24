def classify_ip_risk(text: str, restricted_terms) -> str:
    lowered = text.lower()

    for t in restricted_terms:
        if t.lower() in lowered:
            return "high"

    if len(text.split()) < 5:
        return "low"

    return "medium"
