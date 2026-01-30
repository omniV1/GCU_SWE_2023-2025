# agents/classifiers.py

import numpy as np

class BugGateClassifier:
    """Classifies code for Bug quality gate using different activation functions"""

    def __init__(self, verbose=True):
        self.name = "Bug Gate Classifier"
        self.activation_function = 'relu'  # Default
        self.verbose = verbose

    def classify(self, features, activation='relu'):
        """
        Classify code as PASS or FAIL for bug gate

        Args:
            features (dict): Bug features from NLP agent
            activation (str): 'sigmoid' or 'relu'

        Returns:
            str: 'PASS' or 'FAIL'
        """
        self.activation_function = activation

        # Extract key metrics
        max_complexity = features.get('max_complexity', 0)
        max_nesting = features.get('max_nesting', 0)
        max_function_length = features.get('max_function_length', 0)

        if activation == 'sigmoid':
            return self._classify_sigmoid(max_complexity, max_nesting, max_function_length)
        elif activation == 'relu':
            return self._classify_relu(max_complexity, max_nesting, max_function_length)
        else:
            raise ValueError(f"Unknown activation: {activation}")
    
    def _classify_sigmoid(self, complexity, nesting, length):
        """Soft threshold classification using sigmoid"""
        # Weighted score
        score = (
            0.4 * self._sigmoid(complexity - 10) +
            0.3 * self._sigmoid(nesting - 3) +
            0.3 * self._sigmoid(length - 50)
        )
        
        threshold = 0.6
        result = 'FAIL' if score > threshold else 'PASS'
        if self.verbose:
            print(f"[Bug Classifier - Sigmoid] Score: {score:.3f}, Threshold: {threshold}, Result: {result}")
        return result
    
    def _classify_relu(self, complexity, nesting, length):
        """Hard threshold classification using ReLU-style"""
        # Hard cutoffs
        complexity_threshold = 15
        nesting_threshold = 4
        length_threshold = 100
        
        fail_conditions = [
            complexity > complexity_threshold,
            nesting > nesting_threshold,
            length > length_threshold
        ]
        
        # Fail if any condition is met
        result = 'FAIL' if any(fail_conditions) else 'PASS'
        if self.verbose:
            print(f"[Bug Classifier - ReLU] Complexity: {complexity} (>{complexity_threshold}?), "
                  f"Nesting: {nesting} (>{nesting_threshold}?), "
                  f"Length: {length} (>{length_threshold}?), Result: {result}")
        return result
    
    @staticmethod
    def _sigmoid(x):
        """Sigmoid activation function"""
        return 1 / (1 + np.exp(-x))


class VulnerabilityGateClassifier:
    """Classifies code for Vulnerability quality gate"""

    def __init__(self, verbose=True):
        self.name = "Vulnerability Gate Classifier"
        self.activation_function = 'relu'  # Default
        self.verbose = verbose
    
    def classify(self, features, activation='relu'):
        """
        Classify code as PASS or FAIL for vulnerability gate
        
        Args:
            features (dict): Vulnerability features from NLP agent
            activation (str): 'sigmoid' or 'relu'
            
        Returns:
            str: 'PASS' or 'FAIL'
        """
        self.activation_function = activation
        
        # Extract vulnerability signals
        total_signals = features.get('total_vulnerability_signals', 0)
        eval_usage = features.get('eval_usage', 0)
        sql_concat = features.get('sql_concat', 0)
        hardcoded_secrets = features.get('hardcoded_secrets', 0)
        
        if activation == 'sigmoid':
            return self._classify_sigmoid(total_signals, eval_usage, sql_concat, hardcoded_secrets)
        elif activation == 'relu':
            return self._classify_relu(total_signals, eval_usage, sql_concat, hardcoded_secrets)
        else:
            raise ValueError(f"Unknown activation: {activation}")
    
    def _classify_sigmoid(self, total_signals, eval_usage, sql_concat, secrets):
        """Soft threshold for vulnerability detection"""
        # Weighted score with higher weight on critical vulnerabilities
        score = (
            0.5 * self._sigmoid(total_signals - 1) +
            0.3 * eval_usage +  # Binary: 0 or 1
            0.2 * min(sql_concat / 2, 1)  # Normalize SQL patterns
        )
        
        threshold = 0.5
        result = 'FAIL' if score > threshold else 'PASS'
        if self.verbose:
            print(f"[Vuln Classifier - Sigmoid] Score: {score:.3f}, Threshold: {threshold}, Result: {result}")
        return result
    
    def _classify_relu(self, total_signals, eval_usage, sql_concat, secrets):
        """Hard threshold for vulnerability detection"""
        # Fail if ANY critical vulnerability present
        fail_conditions = [
            total_signals > 0,  # Any vulnerability signal
            eval_usage > 0,     # Eval/exec usage
            sql_concat > 0,     # SQL injection pattern
            secrets > 0         # Hardcoded secrets
        ]
        
        # More strict: fail if any condition is met
        result = 'FAIL' if any(fail_conditions) else 'PASS'
        if self.verbose:
            print(f"[Vuln Classifier - ReLU] Signals: {total_signals}, "
                  f"Eval: {eval_usage}, SQL: {sql_concat}, Secrets: {secrets}, Result: {result}")
        return result
    
    @staticmethod
    def _sigmoid(x):
        """Sigmoid activation function"""
        return 1 / (1 + np.exp(-x))
