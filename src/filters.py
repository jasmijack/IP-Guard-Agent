import re
import yaml

def load_restricted_terms():
    with open("config/restricted_terms.yaml") as f:
        content = yaml.safe_load(f)
    return content["restricted_terms"]

def is_ip_sensitive(text: str, restricted_terms) -> bool:
    pattern = "|".join([re.escape(t) for t in restricted_terms])
    return bool(re.search(pattern, text, flags=re.IGNORECASE))

def filter_docs(docs):
    restricted = load_restricted_terms()
    return [d for d in docs if not is_ip_sensitive(d["content"], restricted)]
