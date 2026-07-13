# agents/nlp_agent.py

import ast
import re
from radon.complexity import cc_visit

class NLPAgent:
    """Extracts deterministic static-analysis features from Python code."""
    
    def __init__(self, verbose=False):
        self.name = "NLP Feature Extraction Agent"
        self.verbose = verbose

    def _log(self, message):
        if self.verbose:
            print(f"[NLP Agent] {message}")
    
    def extract_features(self, code_text, filepath):
        """
        Extract features for Bug and Vulnerability gates
        
        Args:
            code_text (str): Source code as string
            filepath (str): Path to file
            
        Returns:
            dict: Features for both gates
        """
        self._log(f"Extracting features from {filepath}")
        
        try:
            tree = ast.parse(code_text)
        except SyntaxError as e:
            self._log(f"Syntax error in {filepath}: {e}")
            return self._default_features(filepath)
        
        bug_features = self._extract_bug_features(code_text, tree)
        vuln_features = self._extract_vulnerability_features(code_text, tree)
        
        return {
            'bug_features': bug_features,
            'vulnerability_features': vuln_features,
            'filepath': filepath
        }
    
    def _extract_bug_features(self, code_text, tree):
        """Extract features related to bugs (complexity, structure)"""
        
        # Cyclomatic complexity using radon
        try:
            complexity_results = cc_visit(code_text)
            complexities = [r.complexity for r in complexity_results]
            avg_complexity = sum(complexities) / max(len(complexities), 1)
            max_complexity = max(complexities, default=0)
        except (TypeError, ValueError):
            avg_complexity = 0
            max_complexity = 0
        
        # Nesting depth
        max_nesting = self._calculate_max_nesting(tree)
        
        # Function length
        function_lengths = self._calculate_function_lengths(tree)
        avg_function_length = sum(function_lengths) / max(len(function_lengths), 1)
        max_function_length = max(function_lengths, default=0)
        
        # Number of functions
        num_functions = len(function_lengths)
        
        # Lines of code
        lines_of_code = len(code_text.split('\n'))
        
        features = {
            'avg_complexity': round(avg_complexity, 2),
            'max_complexity': max_complexity,
            'max_nesting': max_nesting,
            'avg_function_length': round(avg_function_length, 2),
            'max_function_length': max_function_length,
            'num_functions': num_functions,
            'lines_of_code': lines_of_code
        }
        
        self._log(f"Bug features: {features}")
        return features
    
    def _extract_vulnerability_features(self, code_text, tree):
        """Extract features related to security vulnerabilities"""
        
        # SQL injection patterns
        sql_concat = len(re.findall(r'["\'].*SELECT.*["\'].*\+', code_text, re.IGNORECASE))
        sql_format = len(re.findall(r'["\'].*SELECT.*["\'].*\.format\(', code_text, re.IGNORECASE))
        
        # Dangerous function usage
        eval_usage = int('eval(' in code_text or 'exec(' in code_text)
        pickle_usage = int('pickle.loads' in code_text)
        
        # Hard-coded secrets
        hardcoded_secrets = len(re.findall(
            r'(password|secret|api_key|token)\s*=\s*["\'][^"\']{8,}["\']', 
            code_text, 
            re.IGNORECASE
        ))
        
        # Command injection risks
        os_system = int('os.system(' in code_text)
        shell_true = int('shell=True' in code_text)
        
        # Calculate total vulnerability signals
        total_signals = (
            sql_concat + sql_format + eval_usage + 
            pickle_usage + hardcoded_secrets + os_system + shell_true
        )
        
        features = {
            'sql_concat': sql_concat,
            'sql_format': sql_format,
            'eval_usage': eval_usage,
            'pickle_usage': pickle_usage,
            'hardcoded_secrets': hardcoded_secrets,
            'os_system': os_system,
            'shell_true': shell_true,
            'total_vulnerability_signals': total_signals
        }
        
        self._log(f"Vulnerability features: {features}")
        return features
    
    def _calculate_max_nesting(self, tree):
        """Calculate maximum nesting depth in code"""
        class NestingVisitor(ast.NodeVisitor):
            def __init__(self):
                self.max_depth = 0
                self.current_depth = 0
            
            def visit_If(self, node):
                self.current_depth += 1
                self.max_depth = max(self.max_depth, self.current_depth)
                self.generic_visit(node)
                self.current_depth -= 1
            
            def visit_For(self, node):
                self.current_depth += 1
                self.max_depth = max(self.max_depth, self.current_depth)
                self.generic_visit(node)
                self.current_depth -= 1
            
            def visit_While(self, node):
                self.current_depth += 1
                self.max_depth = max(self.max_depth, self.current_depth)
                self.generic_visit(node)
                self.current_depth -= 1
        
        visitor = NestingVisitor()
        visitor.visit(tree)
        return visitor.max_depth
    
    def _calculate_function_lengths(self, tree):
        """Calculate lengths of all functions in lines"""
        class FunctionVisitor(ast.NodeVisitor):
            def __init__(self):
                self.function_lengths = []
            
            def visit_FunctionDef(self, node):
                # Calculate function length
                if hasattr(node, 'end_lineno') and hasattr(node, 'lineno'):
                    length = node.end_lineno - node.lineno + 1
                    self.function_lengths.append(length)
                self.generic_visit(node)
        
        visitor = FunctionVisitor()
        visitor.visit(tree)
        return visitor.function_lengths if visitor.function_lengths else [0]
    
    def _default_features(self, filepath):
        """Return default features when parsing fails"""
        return {
            'bug_features': {
                'avg_complexity': 0,
                'max_complexity': 0,
                'max_nesting': 0,
                'avg_function_length': 0,
                'max_function_length': 0,
                'num_functions': 0,
                'lines_of_code': 0
            },
            'vulnerability_features': {
                'sql_concat': 0,
                'sql_format': 0,
                'eval_usage': 0,
                'pickle_usage': 0,
                'hardcoded_secrets': 0,
                'os_system': 0,
                'shell_true': 0,
                'total_vulnerability_signals': 0
            },
            'filepath': filepath
        }
