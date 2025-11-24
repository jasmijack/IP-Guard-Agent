from src.filters import filter_docs

def test_safe_filtering():
    docs = [
        {"id": "1", "content": "Internal use only roadmap"},
        {"id": "2", "content": "General product overview"}
    ]

    safe = filter_docs(docs)

    assert len(safe) == 1
    assert safe[0]["id"] == "2"
