from src.policy import classify_ip_risk

def test_policy_levels():
    restricted = ["confidential"]

    assert classify_ip_risk("confidential strategy", restricted) == "high"
    assert classify_ip_risk("hello world", restricted) == "medium"
    assert classify_ip_risk("Hi", restricted) == "low"
