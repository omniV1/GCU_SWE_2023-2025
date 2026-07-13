from agents.nlp_agent import NLPAgent


def test_extracts_python_structure_deterministically():
    code = """\
def choose(value):
    if value > 0:
        for item in range(value):
            return item
    return None
"""

    first = NLPAgent().extract_features(code, "example.py")
    second = NLPAgent().extract_features(code, "example.py")

    assert first == second
    assert first["filepath"] == "example.py"
    assert first["bug_features"] == {
        "avg_complexity": 3.0,
        "max_complexity": 3,
        "max_nesting": 2,
        "avg_function_length": 5.0,
        "max_function_length": 5,
        "num_functions": 1,
        "lines_of_code": 6,
    }
    assert first["vulnerability_features"]["total_vulnerability_signals"] == 0


def test_extracts_each_supported_vulnerability_signal():
    code = """\
import os
import pickle

password = "long-enough-secret"
query = "SELECT * FROM users WHERE id = " + user_input
other = "SELECT * FROM users WHERE name = {}".format(user_input)
eval(user_input)
pickle.loads(payload)
os.system(command)
subprocess.run(command, shell=True)
"""

    features = NLPAgent().extract_features(code, "unsafe.py")[
        "vulnerability_features"
    ]

    assert features == {
        "sql_concat": 1,
        "sql_format": 1,
        "eval_usage": 1,
        "pickle_usage": 1,
        "hardcoded_secrets": 1,
        "os_system": 1,
        "shell_true": 1,
        "total_vulnerability_signals": 7,
    }


def test_invalid_python_returns_documented_defaults():
    features = NLPAgent().extract_features("def broken(:\n", "broken.py")

    assert features["filepath"] == "broken.py"
    assert features["bug_features"]["num_functions"] == 0
    assert features["bug_features"]["lines_of_code"] == 0
    assert features["vulnerability_features"]["total_vulnerability_signals"] == 0


def test_library_is_quiet_by_default(capsys):
    NLPAgent().extract_features("value = 1\n", "quiet.py")

    assert capsys.readouterr().out == ""
