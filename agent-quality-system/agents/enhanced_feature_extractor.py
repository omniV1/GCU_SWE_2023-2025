# agents/enhanced_feature_extractor.py
"""
Enhanced Feature Extractor for All 8 Quality Gates
Extracts features for: Bugs, Vulnerabilities, Security Hotspots, 
Reliability, Security, Maintainability, Coverage, Duplication
"""

import os
import re
import ast
import hashlib
from pathlib import Path
from collections import defaultdict

try:
    from radon.complexity import cc_visit
    HAS_RADON = True
except ImportError:
    HAS_RADON = False


class EnhancedFeatureExtractor:
    """Comprehensive feature extraction for all quality gates"""
    
    # Security hotspot patterns (need manual review)
    HOTSPOT_PATTERNS = {
        'crypto': [
            r'from\s+cryptography',
            r'import\s+hashlib',
            r'import\s+hmac',
            r'\.encrypt\(',
            r'\.decrypt\(',
            r'AES\.',
            r'RSA\.',
        ],
        'file_ops': [
            r'open\s*\([^)]*["\']w',
            r'\.write\s*\(',
            r'shutil\.(copy|move|rmtree)',
            r'os\.(remove|unlink|rmdir)',
        ],
        'network': [
            r'socket\.',
            r'requests\.(get|post|put|delete)',
            r'urllib',
            r'http\.client',
            r'ftplib',
        ],
        'random': [
            r'random\.(random|randint|choice)',  # Not cryptographically secure
        ],
        'serialization': [
            r'pickle\.(load|loads)',
            r'yaml\.load\(',
            r'marshal\.load',
        ],
        'logging': [
            r'print\s*\([^)]*password',
            r'logging\.[^(]+\([^)]*password',
        ]
    }
    
    # API key patterns for secrets detection
    SECRET_PATTERNS = [
        r'AIzaSy[a-zA-Z0-9_-]{33}',  # Google API
        r'sk_live_[a-zA-Z0-9]{24,}',  # Stripe live
        r'sk_test_[a-zA-Z0-9]{24,}',  # Stripe test
        r'AKIA[A-Z0-9]{16}',  # AWS Access Key
        r'ghp_[a-zA-Z0-9]{36}',  # GitHub PAT
        r'xox[baprs]-[a-zA-Z0-9-]+',  # Slack
        r'ya29\.[a-zA-Z0-9_-]+',  # Google OAuth
        r'eyJ[a-zA-Z0-9_-]*\.eyJ[a-zA-Z0-9_-]*\.',  # JWT tokens
        r'(password|secret|api_key|apikey|token|auth)\s*[=:]\s*["\'][^"\']{8,}["\']',
    ]
    
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.name = "Enhanced Feature Extractor"
    
    def log(self, message):
        if self.verbose:
            print(f"[{self.name}] {message}")
    
    def extract_all_features(self, code_text, filepath):
        """Extract comprehensive features for all 8 quality gates"""
        language = self._detect_language(filepath)
        
        features = {
            'filepath': filepath,
            'language': language,
            'bug_features': self._extract_bug_features(code_text, language),
            'vulnerability_features': self._extract_vulnerability_features(code_text, language),
            'security_hotspot_features': self._extract_hotspot_features(code_text),
            'project_features': self._extract_project_features(code_text, filepath),
        }
        
        # Calculate total signals
        vuln = features['vulnerability_features']
        vuln['total_vulnerability_signals'] = (
            vuln.get('sql_injection', 0) +
            vuln.get('eval_exec', 0) +
            vuln.get('command_injection', 0) +
            vuln.get('hardcoded_secrets', 0) +
            vuln.get('xss_risk', 0)
        )
        
        return features
    
    def _detect_language(self, filepath):
        """Detect programming language from file extension"""
        ext_map = {
            '.py': 'python',
            '.java': 'java',
            '.cs': 'csharp',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.tsx': 'typescript',
            '.jsx': 'javascript',
            '.c': 'c',
            '.cpp': 'cpp',
            '.h': 'c',
        }
        ext = os.path.splitext(filepath)[1].lower()
        return ext_map.get(ext, 'unknown')
    
    def _extract_bug_features(self, code_text, language):
        """Extract bug-related features (complexity, nesting, etc.)"""
        features = {
            'avg_complexity': 0,
            'max_complexity': 0,
            'max_nesting': 0,
            'avg_function_length': 0,
            'max_function_length': 0,
            'num_functions': 0,
            'lines_of_code': len(code_text.split('\n')),
            'error_handling_score': 50,  # Default medium
        }
        
        if language == 'python' and HAS_RADON:
            try:
                tree = ast.parse(code_text)
                
                # Complexity
                complexity_results = cc_visit(code_text)
                if complexity_results:
                    complexities = [r.complexity for r in complexity_results]
                    features['avg_complexity'] = round(sum(complexities) / len(complexities), 2)
                    features['max_complexity'] = max(complexities)
                
                # Nesting
                features['max_nesting'] = self._calculate_nesting(tree)
                
                # Function lengths
                lengths = self._calculate_function_lengths(tree)
                if lengths:
                    features['avg_function_length'] = round(sum(lengths) / len(lengths), 2)
                    features['max_function_length'] = max(lengths)
                    features['num_functions'] = len(lengths)
                
                # Error handling
                features['error_handling_score'] = self._calculate_error_handling_score(code_text)
                
            except SyntaxError:
                pass
        else:
            # Generic analysis for other languages
            features.update(self._generic_bug_features(code_text, language))
        
        return features
    
    def _extract_vulnerability_features(self, code_text, language):
        """Extract vulnerability-related features"""
        features = {
            'sql_injection': 0,
            'eval_exec': 0,
            'command_injection': 0,
            'hardcoded_secrets': 0,
            'xss_risk': 0,
            'path_traversal': 0,
            'xxe_risk': 0,
            'insecure_deserialization': 0,
        }
        
        # SQL Injection patterns
        features['sql_injection'] = (
            len(re.findall(r'["\'].*SELECT.*["\'].*[\+\%]', code_text, re.IGNORECASE)) +
            len(re.findall(r'["\'].*SELECT.*["\'].*\.format\(', code_text, re.IGNORECASE)) +
            len(re.findall(r'f["\'].*SELECT.*\{', code_text, re.IGNORECASE))
        )
        
        # Eval/Exec usage
        features['eval_exec'] = int(
            'eval(' in code_text or 
            'exec(' in code_text or
            'Function(' in code_text
        )
        
        # Command Injection
        features['command_injection'] = int(
            'os.system(' in code_text or
            'shell=True' in code_text or
            'subprocess.call' in code_text or
            'child_process' in code_text or
            'Runtime.getRuntime().exec' in code_text
        )
        
        # Hardcoded secrets (enhanced)
        for pattern in self.SECRET_PATTERNS:
            features['hardcoded_secrets'] += len(re.findall(pattern, code_text, re.IGNORECASE))
        
        # XSS Risk
        features['xss_risk'] = (
            len(re.findall(r'\.innerHTML\s*=', code_text)) +
            len(re.findall(r'dangerouslySetInnerHTML', code_text)) +
            len(re.findall(r'document\.write\(', code_text))
        )
        
        # Path Traversal
        features['path_traversal'] = int(
            '../' in code_text and 'open(' in code_text
        )
        
        # XXE Risk
        features['xxe_risk'] = int(
            'XMLParser' in code_text or
            'etree.parse' in code_text or
            'DocumentBuilder' in code_text
        )
        
        # Insecure Deserialization
        features['insecure_deserialization'] = int(
            'pickle.loads' in code_text or
            'yaml.load(' in code_text or
            'readObject(' in code_text
        )
        
        return features
    
    def _extract_hotspot_features(self, code_text):
        """Extract security hotspot features (need manual review)"""
        features = {
            'security_hotspots': 0,
            'crypto_usage': 0,
            'file_operations': 0,
            'network_operations': 0,
            'weak_random': 0,
            'serialization_risk': 0,
            'sensitive_logging': 0,
        }
        
        for category, patterns in self.HOTSPOT_PATTERNS.items():
            count = 0
            for pattern in patterns:
                count += len(re.findall(pattern, code_text, re.IGNORECASE))
            
            if category == 'crypto':
                features['crypto_usage'] = count
            elif category == 'file_ops':
                features['file_operations'] = count
            elif category == 'network':
                features['network_operations'] = count
            elif category == 'random':
                features['weak_random'] = count
            elif category == 'serialization':
                features['serialization_risk'] = count
            elif category == 'logging':
                features['sensitive_logging'] = count
            
            features['security_hotspots'] += count
        
        return features
    
    def _extract_project_features(self, code_text, filepath):
        """Extract project-level features (coverage, duplication indicators)"""
        features = {
            'has_test_files': 0,
            'test_file_ratio': 0,
            'has_test_framework': 0,
            'duplication_ratio': 0,
            'duplicate_blocks': 0,
            'has_tests': 0,
        }
        
        # Check if this IS a test file
        filename = os.path.basename(filepath).lower()
        if 'test' in filename or '_test' in filename or 'spec' in filename:
            features['has_test_files'] = 1
            features['has_tests'] = 1
        
        # Check for test framework imports
        test_frameworks = ['pytest', 'unittest', 'nose', 'jest', 'mocha', 'junit', 'nunit', 'xunit']
        for framework in test_frameworks:
            if framework in code_text.lower():
                features['has_test_framework'] = 1
                break
        
        # Calculate duplication (simplified - look for repeated blocks)
        features['duplication_ratio'] = self._calculate_duplication(code_text)
        
        return features
    
    def _calculate_nesting(self, tree):
        """Calculate maximum nesting depth"""
        class NestingVisitor(ast.NodeVisitor):
            def __init__(self):
                self.max_depth = 0
                self.current_depth = 0
            
            def _visit_block(self, node):
                self.current_depth += 1
                self.max_depth = max(self.max_depth, self.current_depth)
                self.generic_visit(node)
                self.current_depth -= 1
            
            def visit_If(self, node): self._visit_block(node)
            def visit_For(self, node): self._visit_block(node)
            def visit_While(self, node): self._visit_block(node)
            def visit_With(self, node): self._visit_block(node)
            def visit_Try(self, node): self._visit_block(node)
        
        visitor = NestingVisitor()
        visitor.visit(tree)
        return visitor.max_depth
    
    def _calculate_function_lengths(self, tree):
        """Calculate function lengths"""
        lengths = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if hasattr(node, 'end_lineno') and hasattr(node, 'lineno'):
                    lengths.append(node.end_lineno - node.lineno + 1)
        return lengths if lengths else [0]
    
    def _calculate_error_handling_score(self, code_text):
        """Calculate error handling coverage (0-100)"""
        total_functions = len(re.findall(r'def\s+\w+\s*\(', code_text))
        try_blocks = len(re.findall(r'\btry\s*:', code_text))
        
        if total_functions == 0:
            return 50
        
        # Score based on try/function ratio
        ratio = min(try_blocks / max(total_functions, 1), 1.0)
        return int(ratio * 100)
    
    def _calculate_duplication(self, code_text):
        """Calculate approximate duplication ratio"""
        lines = [l.strip() for l in code_text.split('\n') if l.strip() and not l.strip().startswith('#')]
        
        if len(lines) < 10:
            return 0.0
        
        # Count duplicate lines (simplified)
        line_counts = defaultdict(int)
        for line in lines:
            if len(line) > 20:  # Only count substantial lines
                line_counts[line] += 1
        
        duplicates = sum(count - 1 for count in line_counts.values() if count > 1)
        return round(duplicates / len(lines) * 100, 1)
    
    def _generic_bug_features(self, code_text, language):
        """Generic bug feature extraction for non-Python languages"""
        features = {}
        
        # Count functions/methods
        if language in ['java', 'csharp']:
            pattern = r'(public|private|protected)\s+\w+\s+\w+\s*\([^)]*\)\s*\{'
        elif language in ['javascript', 'typescript']:
            pattern = r'(function\s+\w+|const\s+\w+\s*=\s*(?:async\s*)?\([^)]*\)\s*=>|\w+\s*\([^)]*\)\s*\{)'
        else:
            pattern = r'\w+\s*\([^)]*\)\s*\{'
        
        num_functions = len(re.findall(pattern, code_text))
        features['num_functions'] = num_functions
        
        # Estimate complexity from decision keywords
        decision_keywords = len(re.findall(r'\b(if|else|for|while|switch|case|catch|&&|\|\||\?)\b', code_text))
        features['avg_complexity'] = round(decision_keywords / max(num_functions, 1), 2)
        features['max_complexity'] = min(decision_keywords // max(num_functions, 1) + 5, 50)
        
        # Calculate nesting from braces
        features['max_nesting'] = self._calculate_brace_nesting(code_text)
        
        # Estimate function length
        features['avg_function_length'] = 20  # Default estimate
        features['max_function_length'] = 50  # Default estimate
        features['error_handling_score'] = 50
        
        return features
    
    def _calculate_brace_nesting(self, code_text):
        """Calculate nesting depth from braces"""
        max_depth = 0
        current_depth = 0
        
        for char in code_text:
            if char == '{':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == '}':
                current_depth = max(0, current_depth - 1)
        
        return max_depth
