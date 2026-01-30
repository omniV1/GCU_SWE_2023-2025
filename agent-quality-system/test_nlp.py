# test_nlp.py
from agents.nlp_agent import NLPAgent

# Sample code to test
sample_code = """
def complex_function(a, b, c):
    if a > 0:
        if b > 0:
            if c > 0:
                for i in range(10):
                    for j in range(10):
                        print(i + j)
    return a + b + c

query = "SELECT * FROM users WHERE id = " + user_input
password = "hardcoded_secret_123"
"""

nlp = NLPAgent()
features = nlp.extract_features(sample_code, "test.py")

print("\nExtracted Features:")
print(f"Bug Features: {features['bug_features']}")
print(f"Vulnerability Features: {features['vulnerability_features']}")
