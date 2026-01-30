# test_classifiers.py
from agents.nlp_agent import NLPAgent
from agents.classifiers import BugGateClassifier, VulnerabilityGateClassifier

# Test code with known issues
bad_code = """
def overly_complex_function(a, b, c, d, e):
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        for i in range(100):
                            for j in range(100):
                                for k in range(100):
                                    print(i + j + k)
    query = "SELECT * FROM users WHERE id = " + user_input
    password = "super_secret_password_123"
    eval(user_code)
    return a + b + c + d + e
"""

# Extract features
nlp = NLPAgent()
features = nlp.extract_features(bad_code, "bad_code.py")

# Test Bug Gate
print("\n=== BUG GATE TESTING ===")
bug_classifier = BugGateClassifier()

print("\nTesting with Sigmoid:")
result_sigmoid = bug_classifier.classify(features['bug_features'], activation='sigmoid')
print(f"Result: {result_sigmoid}")

print("\nTesting with ReLU:")
result_relu = bug_classifier.classify(features['bug_features'], activation='relu')
print(f"Result: {result_relu}")

# Test Vulnerability Gate
print("\n=== VULNERABILITY GATE TESTING ===")
vuln_classifier = VulnerabilityGateClassifier()

print("\nTesting with Sigmoid:")
result_sigmoid = vuln_classifier.classify(features['vulnerability_features'], activation='sigmoid')
print(f"Result: {result_sigmoid}")

print("\nTesting with ReLU:")
result_relu = vuln_classifier.classify(features['vulnerability_features'], activation='relu')
print(f"Result: {result_relu}")
