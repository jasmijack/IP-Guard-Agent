from filters import load_restricted_terms
from policy import classify_ip_risk

def evaluate_corpus(docs):
    restricted = load_restricted_terms()
    results = []

    for d in docs:
        risk = classify_ip_risk(d["content"], restricted)
        results.append({
            "id": d["id"],
            "risk_level": risk,
            "snippet": d["content"][:80]
        })

    return results
