import json
from openai import OpenAI
from filters import filter_docs

client = OpenAI()

def load_docs():
    with open("data/sample_docs.json") as f:
        return json.load(f)

def retrieve_safe_docs():
    docs = load_docs()
    return filter_docs(docs)

def answer_query(query):
    safe_docs = retrieve_safe_docs()

    prompt = f"""
You are an IP aware assistant. Avoid exposing or generating content that may violate 
company confidentiality or trade secret boundaries.

User query: {query}

Safe documents:
{safe_docs}
"""

    resp = client.chat.completions.create(
        model="gpt-5.1",
        messages=[{"role": "user", "content": prompt}]
    )

    return resp.choices[0].message["content"]
