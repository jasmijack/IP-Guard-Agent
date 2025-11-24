from src.filters import is_ip_sensitive, load_restricted_terms

def test_ip_detection():
    terms = load_restricted_terms()
    assert is_ip_sensitive("This is confidential", terms) is True
    assert is_ip_sensitive("Public info for all audiences", terms) is False
