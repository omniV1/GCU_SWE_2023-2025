import pytest

from agents.all_gate_classifiers import (
    AllGatesClassificationPipeline,
    BugGateClassifier,
    VulnerabilityGateClassifier,
)


@pytest.mark.parametrize("activation", ["relu", "sigmoid"])
def test_bug_classifier_passes_low_risk_features(activation):
    features = {
        "max_complexity": 1,
        "max_nesting": 0,
        "max_function_length": 5,
    }

    assert BugGateClassifier().classify(features, activation) == "PASS"


@pytest.mark.parametrize("activation", ["relu", "sigmoid"])
def test_bug_classifier_fails_high_risk_features(activation):
    features = {
        "max_complexity": 30,
        "max_nesting": 8,
        "max_function_length": 200,
    }

    assert BugGateClassifier().classify(features, activation) == "FAIL"


@pytest.mark.parametrize("activation", ["relu", "sigmoid"])
def test_vulnerability_classifier_distinguishes_clean_and_flagged_code(activation):
    classifier = VulnerabilityGateClassifier()
    clean = {"total_vulnerability_signals": 0}
    flagged = {
        "total_vulnerability_signals": 2,
        "eval_exec": 1,
        "sql_injection": 1,
    }

    assert classifier.classify(clean, activation) == "PASS"
    assert classifier.classify(flagged, activation) == "FAIL"


def test_classifier_rejects_unknown_activation():
    with pytest.raises(ValueError, match="Unknown activation"):
        BugGateClassifier().classify({}, "softmax")


def test_pipeline_uses_defaults_when_config_is_omitted():
    pipeline = AllGatesClassificationPipeline()

    assert pipeline.get_gate_names() == [
        "bug_gate",
        "vulnerability_gate",
        "security_hotspot_gate",
        "reliability_gate",
        "security_gate",
        "maintainability_gate",
        "coverage_gate",
        "duplication_gate",
    ]


def test_pipeline_honors_explicit_activation_configuration():
    pipeline = AllGatesClassificationPipeline(
        {"bug_gate": {"activation": "sigmoid"}}
    )

    assert pipeline.activations["bug_gate"] == "sigmoid"
    assert pipeline.activations["security_gate"] == "relu"
