# agents/all_gate_classifiers.py
"""
Comprehensive Quality Gate Classifiers
Supports all 8 SonarQube quality gates with Sigmoid/ReLU activation selection.
"""

import numpy as np
import re
import hashlib
from collections import defaultdict


class BaseClassifier:
    """Base class for all quality gate classifiers"""
    
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.activation_function = 'relu'
    
    def log(self, message):
        if self.verbose:
            print(message)
    
    @staticmethod
    def sigmoid(x):
        """Sigmoid activation function"""
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))


class BugGateClassifier(BaseClassifier):
    """Classifies code for Bug quality gate"""
    
    def __init__(self, verbose=False):
        super().__init__(verbose)
        self.name = "Bug Gate Classifier"
    
    def classify(self, features, activation='relu'):
        self.activation_function = activation
        
        max_complexity = features.get('max_complexity', 0)
        max_nesting = features.get('max_nesting', 0)
        max_function_length = features.get('max_function_length', 0)
        
        if activation == 'sigmoid':
            return self._classify_sigmoid(max_complexity, max_nesting, max_function_length)
        else:
            return self._classify_relu(max_complexity, max_nesting, max_function_length)
    
    def _classify_sigmoid(self, complexity, nesting, length):
        score = (
            0.4 * self.sigmoid(complexity - 10) +
            0.3 * self.sigmoid(nesting - 3) +
            0.3 * self.sigmoid(length - 50)
        )
        threshold = 0.6
        result = 'FAIL' if score > threshold else 'PASS'
        self.log(f"[Bug Classifier - Sigmoid] Score: {score:.3f}, Result: {result}")
        return result
    
    def _classify_relu(self, complexity, nesting, length):
        fail_conditions = [
            complexity > 15,
            nesting > 4,
            length > 100
        ]
        result = 'FAIL' if any(fail_conditions) else 'PASS'
        self.log(f"[Bug Classifier - ReLU] Complexity: {complexity}, Nesting: {nesting}, Result: {result}")
        return result


class VulnerabilityGateClassifier(BaseClassifier):
    """Classifies code for Vulnerability quality gate"""
    
    def __init__(self, verbose=False):
        super().__init__(verbose)
        self.name = "Vulnerability Gate Classifier"
    
    def classify(self, features, activation='relu'):
        self.activation_function = activation
        
        total_signals = features.get('total_vulnerability_signals', 0)
        eval_usage = features.get('eval_exec', features.get('eval_usage', 0))
        sql_injection = features.get('sql_injection', features.get('sql_concat', 0))
        secrets = features.get('hardcoded_secrets', 0)
        
        if activation == 'sigmoid':
            return self._classify_sigmoid(total_signals, eval_usage, sql_injection, secrets)
        else:
            return self._classify_relu(total_signals, eval_usage, sql_injection, secrets)
    
    def _classify_sigmoid(self, total_signals, eval_usage, sql_injection, secrets):
        score = (
            0.5 * self.sigmoid(total_signals - 1) +
            0.3 * eval_usage +
            0.2 * min(sql_injection / 2, 1)
        )
        threshold = 0.5
        result = 'FAIL' if score > threshold else 'PASS'
        self.log(f"[Vuln Classifier - Sigmoid] Score: {score:.3f}, Result: {result}")
        return result
    
    def _classify_relu(self, total_signals, eval_usage, sql_injection, secrets):
        fail_conditions = [
            total_signals > 0,
            eval_usage > 0,
            sql_injection > 0,
            secrets > 0
        ]
        result = 'FAIL' if any(fail_conditions) else 'PASS'
        self.log(f"[Vuln Classifier - ReLU] Signals: {total_signals}, Result: {result}")
        return result


class SecurityHotspotClassifier(BaseClassifier):
    """Classifies code for Security Hotspot gate - code that needs manual review"""
    
    def __init__(self, verbose=False):
        super().__init__(verbose)
        self.name = "Security Hotspot Classifier"
    
    def classify(self, features, activation='relu'):
        self.activation_function = activation
        
        # Security hotspots are patterns that MIGHT be issues
        hotspot_patterns = features.get('security_hotspots', 0)
        crypto_usage = features.get('crypto_usage', 0)
        file_operations = features.get('file_operations', 0)
        network_operations = features.get('network_operations', 0)
        random_usage = features.get('weak_random', 0)
        
        total = hotspot_patterns + crypto_usage + file_operations + network_operations + random_usage
        
        if activation == 'sigmoid':
            score = self.sigmoid(total - 2)
            threshold = 0.5
            result = 'FAIL' if score > threshold else 'PASS'
            self.log(f"[Hotspot Classifier - Sigmoid] Score: {score:.3f}, Result: {result}")
        else:
            result = 'FAIL' if total > 0 else 'PASS'
            self.log(f"[Hotspot Classifier - ReLU] Hotspots: {total}, Result: {result}")
        
        return result


class ReliabilityGateClassifier(BaseClassifier):
    """Classifies code for Reliability gate based on bug density and severity"""
    
    def __init__(self, verbose=False):
        super().__init__(verbose)
        self.name = "Reliability Gate Classifier"
    
    def classify(self, features, activation='relu'):
        self.activation_function = activation
        
        # Reliability is based on bug indicators
        complexity = features.get('max_complexity', 0)
        nesting = features.get('max_nesting', 0)
        error_handling = features.get('error_handling_score', 100)  # Higher is better
        code_coverage_indicator = features.get('has_tests', 0)
        
        # Calculate reliability score (0-100, higher is better)
        reliability_score = 100
        reliability_score -= min(complexity * 2, 30)  # Complexity penalty
        reliability_score -= min(nesting * 5, 25)  # Nesting penalty
        reliability_score -= (100 - error_handling) * 0.2  # Error handling penalty
        reliability_score += code_coverage_indicator * 20  # Test bonus
        
        if activation == 'sigmoid':
            # Convert to 0-1 scale, fail if below 0.5
            normalized = reliability_score / 100
            score = self.sigmoid((normalized - 0.6) * 10)
            result = 'FAIL' if score < 0.5 else 'PASS'
            self.log(f"[Reliability - Sigmoid] Score: {reliability_score:.1f}, Result: {result}")
        else:
            # Fail if reliability score below 60 (D/E rating)
            result = 'FAIL' if reliability_score < 60 else 'PASS'
            self.log(f"[Reliability - ReLU] Score: {reliability_score:.1f}, Result: {result}")
        
        return result


class SecurityGateClassifier(BaseClassifier):
    """Classifies code for Security gate based on vulnerability severity"""
    
    def __init__(self, verbose=False):
        super().__init__(verbose)
        self.name = "Security Gate Classifier"
    
    def classify(self, features, activation='relu'):
        self.activation_function = activation
        
        # Critical security issues
        sql_injection = features.get('sql_injection', 0)
        command_injection = features.get('command_injection', 0)
        hardcoded_secrets = features.get('hardcoded_secrets', 0)
        eval_exec = features.get('eval_exec', features.get('eval_usage', 0))
        xss_risk = features.get('xss_risk', 0)
        
        # Weight by severity
        critical_issues = sql_injection + command_injection + hardcoded_secrets
        high_issues = eval_exec + xss_risk
        
        if activation == 'sigmoid':
            score = self.sigmoid(critical_issues * 2 + high_issues - 1)
            result = 'FAIL' if score > 0.5 else 'PASS'
            self.log(f"[Security - Sigmoid] Critical: {critical_issues}, High: {high_issues}, Result: {result}")
        else:
            # Fail on any critical or multiple high issues
            result = 'FAIL' if critical_issues > 0 or high_issues > 1 else 'PASS'
            self.log(f"[Security - ReLU] Critical: {critical_issues}, High: {high_issues}, Result: {result}")
        
        return result


class MaintainabilityGateClassifier(BaseClassifier):
    """Classifies code for Maintainability gate based on code smells"""
    
    def __init__(self, verbose=False):
        super().__init__(verbose)
        self.name = "Maintainability Gate Classifier"
    
    def classify(self, features, activation='relu'):
        self.activation_function = activation
        
        # Code smell indicators
        avg_complexity = features.get('avg_complexity', 0)
        avg_function_length = features.get('avg_function_length', 0)
        num_functions = features.get('num_functions', 1)
        lines_of_code = features.get('lines_of_code', 0)
        
        # Calculate maintainability index (simplified)
        # Lower complexity and shorter functions = better maintainability
        complexity_ratio = avg_complexity / 10 if avg_complexity < 10 else 1.0
        length_ratio = avg_function_length / 30 if avg_function_length < 30 else 1.0
        
        # Score 0-100 (100 is best)
        maintainability_score = 100 * (1 - (complexity_ratio * 0.5 + length_ratio * 0.5))
        
        if activation == 'sigmoid':
            normalized = maintainability_score / 100
            score = self.sigmoid((normalized - 0.5) * 10)
            result = 'FAIL' if score < 0.5 else 'PASS'
            self.log(f"[Maintainability - Sigmoid] Score: {maintainability_score:.1f}, Result: {result}")
        else:
            # Fail if maintainability below 40 (D/E rating)
            result = 'FAIL' if maintainability_score < 40 else 'PASS'
            self.log(f"[Maintainability - ReLU] Score: {maintainability_score:.1f}, Result: {result}")
        
        return result


class CoverageGateClassifier(BaseClassifier):
    """Classifies code for Coverage gate based on test presence"""
    
    def __init__(self, verbose=False):
        super().__init__(verbose)
        self.name = "Coverage Gate Classifier"
    
    def classify(self, features, activation='relu'):
        self.activation_function = activation
        
        # Check for test indicators
        has_test_files = features.get('has_test_files', 0)
        test_file_ratio = features.get('test_file_ratio', 0)  # test files / source files
        has_test_framework = features.get('has_test_framework', 0)
        
        # Estimate coverage (0-100)
        estimated_coverage = 0
        if has_test_files:
            estimated_coverage = min(test_file_ratio * 100, 80)
        if has_test_framework:
            estimated_coverage += 10
        
        if activation == 'sigmoid':
            normalized = estimated_coverage / 100
            score = self.sigmoid((normalized - 0.8) * 10)  # Target 80%
            result = 'FAIL' if score < 0.5 else 'PASS'
            self.log(f"[Coverage - Sigmoid] Est. Coverage: {estimated_coverage:.1f}%, Result: {result}")
        else:
            # Fail if coverage below 80% (SonarQube default)
            result = 'FAIL' if estimated_coverage < 80 else 'PASS'
            self.log(f"[Coverage - ReLU] Est. Coverage: {estimated_coverage:.1f}%, Result: {result}")
        
        return result


class DuplicationGateClassifier(BaseClassifier):
    """Classifies code for Duplication gate"""
    
    def __init__(self, verbose=False):
        super().__init__(verbose)
        self.name = "Duplication Gate Classifier"
    
    def classify(self, features, activation='relu'):
        self.activation_function = activation
        
        # Duplication metrics
        duplication_ratio = features.get('duplication_ratio', 0)  # 0-100%
        duplicate_blocks = features.get('duplicate_blocks', 0)
        
        if activation == 'sigmoid':
            score = self.sigmoid((duplication_ratio - 3) * 2)  # Target < 3%
            result = 'FAIL' if score > 0.5 else 'PASS'
            self.log(f"[Duplication - Sigmoid] Ratio: {duplication_ratio:.1f}%, Result: {result}")
        else:
            # Fail if duplication above 3% (SonarQube default)
            result = 'FAIL' if duplication_ratio > 3 else 'PASS'
            self.log(f"[Duplication - ReLU] Ratio: {duplication_ratio:.1f}%, Result: {result}")
        
        return result


class AllGatesClassificationPipeline:
    """Comprehensive classification pipeline for all 8 quality gates"""
    
    def __init__(self, config=None, verbose=False):
        self.verbose = verbose
        self.config = config or {}
        
        # Initialize all classifiers
        self.classifiers = {
            'bug_gate': BugGateClassifier(verbose),
            'vulnerability_gate': VulnerabilityGateClassifier(verbose),
            'security_hotspot_gate': SecurityHotspotClassifier(verbose),
            'reliability_gate': ReliabilityGateClassifier(verbose),
            'security_gate': SecurityGateClassifier(verbose),
            'maintainability_gate': MaintainabilityGateClassifier(verbose),
            'coverage_gate': CoverageGateClassifier(verbose),
            'duplication_gate': DuplicationGateClassifier(verbose),
        }
        
        # Default activations (can be optimized during training)
        self.activations = {
            'bug_gate': config.get('bug_gate', {}).get('activation', 'relu'),
            'vulnerability_gate': config.get('vulnerability_gate', {}).get('activation', 'relu'),
            'security_hotspot_gate': config.get('security_hotspot_gate', {}).get('activation', 'relu'),
            'reliability_gate': config.get('reliability_gate', {}).get('activation', 'relu'),
            'security_gate': config.get('security_gate', {}).get('activation', 'relu'),
            'maintainability_gate': config.get('maintainability_gate', {}).get('activation', 'relu'),
            'coverage_gate': config.get('coverage_gate', {}).get('activation', 'relu'),
            'duplication_gate': config.get('duplication_gate', {}).get('activation', 'relu'),
        }
    
    def classify(self, bug_features, vuln_features, project_features=None):
        """Classify code through all 8 gates"""
        project_features = project_features or {}
        
        results = {}
        
        # Bug Gate
        results['bug_gate'] = self.classifiers['bug_gate'].classify(
            bug_features, self.activations['bug_gate']
        )
        
        # Vulnerability Gate
        results['vulnerability_gate'] = self.classifiers['vulnerability_gate'].classify(
            vuln_features, self.activations['vulnerability_gate']
        )
        
        # Security Hotspot Gate
        results['security_hotspot_gate'] = self.classifiers['security_hotspot_gate'].classify(
            vuln_features, self.activations['security_hotspot_gate']
        )
        
        # Reliability Gate (uses bug features)
        results['reliability_gate'] = self.classifiers['reliability_gate'].classify(
            {**bug_features, **project_features}, self.activations['reliability_gate']
        )
        
        # Security Gate (uses vulnerability features)
        results['security_gate'] = self.classifiers['security_gate'].classify(
            vuln_features, self.activations['security_gate']
        )
        
        # Maintainability Gate (uses bug features)
        results['maintainability_gate'] = self.classifiers['maintainability_gate'].classify(
            bug_features, self.activations['maintainability_gate']
        )
        
        # Coverage Gate (uses project features)
        results['coverage_gate'] = self.classifiers['coverage_gate'].classify(
            project_features, self.activations['coverage_gate']
        )
        
        # Duplication Gate (uses project features)
        results['duplication_gate'] = self.classifiers['duplication_gate'].classify(
            project_features, self.activations['duplication_gate']
        )
        
        # Overall result
        results['overall'] = 'PASS' if all(v == 'PASS' for v in results.values()) else 'FAIL'
        
        return results
    
    def get_gate_names(self):
        """Return list of all gate names"""
        return list(self.classifiers.keys())
