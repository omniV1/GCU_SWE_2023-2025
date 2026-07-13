import pytest

from agents.enhanced_feature_extractor import EnhancedFeatureExtractor


def test_python_feature_extraction_covers_all_feature_groups():
    code = """\
import hashlib
import random
import requests

password = "a-long-static-password"
query = "SELECT * FROM users WHERE id = " + user_input
eval(user_input)
requests.get(url)
random.choice(values)
"""

    features = EnhancedFeatureExtractor().extract_all_features(code, "service.py")

    assert features["language"] == "python"
    assert features["vulnerability_features"]["sql_injection"] == 1
    assert features["vulnerability_features"]["eval_exec"] == 1
    assert features["vulnerability_features"]["hardcoded_secrets"] == 1
    assert features["vulnerability_features"]["total_vulnerability_signals"] == 3
    assert features["security_hotspot_features"]["crypto_usage"] == 1
    assert features["security_hotspot_features"]["network_operations"] == 1
    assert features["security_hotspot_features"]["weak_random"] == 1


@pytest.mark.parametrize(
    ("filename", "language"),
    [
        ("example.py", "python"),
        ("Example.java", "java"),
        ("component.tsx", "typescript"),
        ("module.cpp", "cpp"),
        ("README.md", "unknown"),
    ],
)
def test_language_detection_uses_file_extension(filename, language):
    features = EnhancedFeatureExtractor().extract_all_features("", filename)

    assert features["language"] == language


def test_project_features_recognize_tests_and_framework():
    code = "import pytest\n\ndef test_example():\n    assert True\n"

    project = EnhancedFeatureExtractor().extract_all_features(
        code, "test_example.py"
    )["project_features"]

    assert project["has_test_files"] == 1
    assert project["has_tests"] == 1
    assert project["has_test_framework"] == 1


def test_duplication_ratio_ignores_short_lines_and_counts_substantial_ones():
    repeated = "result = calculate_expensive_value(input_data)"
    code = "\n".join(
        [repeated, repeated] + [f"unique_call_number_{index}(argument)" for index in range(8)]
    )

    project = EnhancedFeatureExtractor().extract_all_features(
        code, "module.js"
    )["project_features"]

    assert project["duplication_ratio"] == 10.0
