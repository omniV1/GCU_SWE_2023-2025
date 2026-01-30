# agents/multi_lang_agent.py
# Multi-language feature extraction agent

import re
import os
from pathlib import Path

class MultiLanguageAgent:
    """Extracts features from multiple programming languages"""
    
    SUPPORTED_LANGUAGES = {
        '.py': 'python',
        '.java': 'java',
        '.cs': 'csharp',
        '.c': 'c',
        '.h': 'c',
        '.cpp': 'cpp',
        '.ts': 'typescript',
        '.js': 'javascript',
        '.tsx': 'typescript',
        '.jsx': 'javascript',
    }
    
    def __init__(self):
        self.name = "Multi-Language Feature Extraction Agent"
    
    def get_language(self, filepath):
        """Detect language from file extension"""
        ext = Path(filepath).suffix.lower()
        return self.SUPPORTED_LANGUAGES.get(ext, 'unknown')
    
    def extract_features(self, code_text, filepath):
        """Extract features based on detected language"""
        language = self.get_language(filepath)
        
        if language == 'unknown':
            return self._default_features(filepath, 'unknown')
        
        # Progress is shown by the caller's progress bar
        # print(f"[Multi-Lang Agent] Analyzing {language}: {os.path.basename(filepath)}")
        
        # Common metrics
        lines_of_code = len([l for l in code_text.split('\n') if l.strip() and not self._is_comment(l, language)])
        
        # Language-specific extraction
        if language == 'python':
            bug_features = self._extract_python_bug_features(code_text)
            vuln_features = self._extract_python_vuln_features(code_text)
        elif language == 'java':
            bug_features = self._extract_java_bug_features(code_text)
            vuln_features = self._extract_java_vuln_features(code_text)
        elif language == 'csharp':
            bug_features = self._extract_csharp_bug_features(code_text)
            vuln_features = self._extract_csharp_vuln_features(code_text)
        elif language == 'c' or language == 'cpp':
            bug_features = self._extract_c_bug_features(code_text)
            vuln_features = self._extract_c_vuln_features(code_text)
        elif language in ('typescript', 'javascript'):
            bug_features = self._extract_js_bug_features(code_text)
            vuln_features = self._extract_js_vuln_features(code_text)
        else:
            bug_features = self._generic_bug_features(code_text)
            vuln_features = self._generic_vuln_features(code_text)
        
        bug_features['lines_of_code'] = lines_of_code
        bug_features['language'] = language
        
        return {
            'bug_features': bug_features,
            'vulnerability_features': vuln_features,
            'filepath': filepath,
            'language': language
        }
    
    def _is_comment(self, line, language):
        """Check if a line is a comment"""
        line = line.strip()
        if not line:
            return True
        
        if language == 'python':
            return line.startswith('#')
        elif language in ('java', 'csharp', 'c', 'cpp', 'javascript', 'typescript'):
            return line.startswith('//') or line.startswith('/*') or line.startswith('*')
        return False
    
    # ==================== PYTHON ====================
    def _extract_python_bug_features(self, code_text):
        """Extract bug-related features from Python code"""
        try:
            from radon.complexity import cc_visit
            complexity_results = cc_visit(code_text)
            complexities = [r.complexity for r in complexity_results]
            avg_complexity = sum(complexities) / max(len(complexities), 1)
            max_complexity = max(complexities, default=0)
        except:
            avg_complexity = 0
            max_complexity = 0
        
        max_nesting = self._calculate_nesting_generic(code_text, 'python')
        num_functions = len(re.findall(r'^\s*def\s+\w+', code_text, re.MULTILINE))
        
        return {
            'avg_complexity': round(avg_complexity, 2),
            'max_complexity': max_complexity,
            'max_nesting': max_nesting,
            'num_functions': num_functions,
        }
    
    def _extract_python_vuln_features(self, code_text):
        """Extract vulnerability features from Python"""
        # Count hardcoded secrets - includes various API key patterns
        # Note: [^\n"\']{8,} prevents matching across line boundaries
        secret_patterns = [
            r'(password|secret|api_key|apikey|token|auth)\s*=\s*["\'][^\n"\']{8,}["\']',  # Generic secrets (single line)
            r'AIzaSy[a-zA-Z0-9_-]{33}',  # Google API keys
            r'sk_live_[a-zA-Z0-9]{24,}',  # Stripe live keys
            r'sk_test_[a-zA-Z0-9]{24,}',  # Stripe test keys
            r'AKIA[A-Z0-9]{16}',  # AWS Access Key IDs
            r'ghp_[a-zA-Z0-9]{36}',  # GitHub personal access tokens
            r'xox[baprs]-[a-zA-Z0-9-]+',  # Slack tokens
        ]
        hardcoded_secrets = sum(len(re.findall(p, code_text, re.IGNORECASE)) for p in secret_patterns)
        
        return {
            'sql_injection': len(re.findall(r'["\'].*SELECT.*["\'].*[\+\%]', code_text, re.IGNORECASE)) +
                            len(re.findall(r'["\'].*SELECT.*["\'].*\.format\(', code_text, re.IGNORECASE)),
            'eval_exec': int('eval(' in code_text or 'exec(' in code_text),
            'hardcoded_secrets': hardcoded_secrets,
            'command_injection': int('os.system(' in code_text or 'shell=True' in code_text or 'subprocess.call' in code_text),
            'pickle_usage': int('pickle.loads' in code_text or 'pickle.load(' in code_text),
            'total_signals': 0  # Will be calculated
        }
    
    # ==================== JAVA ====================
    def _extract_java_bug_features(self, code_text):
        """Extract bug-related features from Java code"""
        # Count methods
        num_methods = len(re.findall(r'(public|private|protected)\s+\w+\s+\w+\s*\([^)]*\)\s*\{', code_text))
        
        # Estimate complexity by counting decision points
        decision_keywords = len(re.findall(r'\b(if|else|for|while|switch|case|catch|&&|\|\||\?)\b', code_text))
        max_complexity = min(decision_keywords // max(num_methods, 1) + 1, 50)
        
        # Calculate nesting
        max_nesting = self._calculate_nesting_generic(code_text, 'java')
        
        return {
            'avg_complexity': round(decision_keywords / max(num_methods, 1), 2),
            'max_complexity': max_complexity,
            'max_nesting': max_nesting,
            'num_functions': num_methods,
        }
    
    def _extract_java_vuln_features(self, code_text):
        """Extract vulnerability features from Java"""
        # SQL Injection
        sql_concat = len(re.findall(r'["\'].*SELECT.*["\'].*\+', code_text, re.IGNORECASE))
        sql_concat += len(re.findall(r'Statement.*execute.*\+', code_text))
        
        # Command Injection
        cmd_injection = int('Runtime.getRuntime().exec(' in code_text or 
                          'ProcessBuilder' in code_text and '.command(' in code_text)
        
        # Hardcoded credentials
        hardcoded = len(re.findall(r'(password|secret|apiKey|token)\s*=\s*"[^"]{8,}"', code_text, re.IGNORECASE))
        
        # Unsafe deserialization
        unsafe_deserial = int('ObjectInputStream' in code_text and 'readObject()' in code_text)
        
        # XXE vulnerability
        xxe = int('XMLInputFactory' in code_text or 'DocumentBuilder' in code_text) and \
              not ('setFeature' in code_text or 'FEATURE_SECURE_PROCESSING' in code_text)
        
        return {
            'sql_injection': sql_concat,
            'eval_exec': 0,  # Java doesn't have eval
            'hardcoded_secrets': hardcoded,
            'command_injection': cmd_injection,
            'unsafe_deserialization': unsafe_deserial,
            'xxe_vulnerability': 1 if xxe else 0,
            'total_signals': 0
        }
    
    # ==================== C# ====================
    def _extract_csharp_bug_features(self, code_text):
        """Extract bug-related features from C# code"""
        # Count methods
        num_methods = len(re.findall(r'(public|private|protected|internal)\s+\w+\s+\w+\s*\([^)]*\)', code_text))
        
        # Estimate complexity
        decision_keywords = len(re.findall(r'\b(if|else|for|foreach|while|switch|case|catch|&&|\|\||\?)\b', code_text))
        max_complexity = min(decision_keywords // max(num_methods, 1) + 1, 50)
        
        max_nesting = self._calculate_nesting_generic(code_text, 'csharp')
        
        return {
            'avg_complexity': round(decision_keywords / max(num_methods, 1), 2),
            'max_complexity': max_complexity,
            'max_nesting': max_nesting,
            'num_functions': num_methods,
        }
    
    def _extract_csharp_vuln_features(self, code_text):
        """Extract vulnerability features from C#"""
        # SQL Injection
        sql_concat = len(re.findall(r'["\'].*SELECT.*["\'].*\+', code_text, re.IGNORECASE))
        sql_concat += len(re.findall(r'SqlCommand.*\+', code_text))
        
        # Command Injection
        cmd_injection = int('Process.Start(' in code_text or 'ProcessStartInfo' in code_text)
        
        # Hardcoded credentials
        hardcoded = len(re.findall(r'(password|secret|apiKey|connectionString)\s*=\s*"[^"]{8,}"', code_text, re.IGNORECASE))
        
        # Unsafe deserialization
        unsafe_deserial = int('BinaryFormatter' in code_text or 'JavaScriptSerializer' in code_text)
        
        # Path traversal
        path_traversal = int('Path.Combine' in code_text and 'Request' in code_text) or \
                        int('..' in code_text and ('File.Read' in code_text or 'File.Write' in code_text))
        
        return {
            'sql_injection': sql_concat,
            'eval_exec': 0,
            'hardcoded_secrets': hardcoded,
            'command_injection': cmd_injection,
            'unsafe_deserialization': unsafe_deserial,
            'path_traversal': 1 if path_traversal else 0,
            'total_signals': 0
        }
    
    # ==================== C/C++ ====================
    def _extract_c_bug_features(self, code_text):
        """Extract bug-related features from C/C++ code"""
        # Count functions
        num_functions = len(re.findall(r'\w+\s+\w+\s*\([^)]*\)\s*\{', code_text))
        
        # Estimate complexity
        decision_keywords = len(re.findall(r'\b(if|else|for|while|switch|case|goto|&&|\|\||\?)\b', code_text))
        max_complexity = min(decision_keywords // max(num_functions, 1) + 1, 50)
        
        max_nesting = self._calculate_nesting_generic(code_text, 'c')
        
        return {
            'avg_complexity': round(decision_keywords / max(num_functions, 1), 2),
            'max_complexity': max_complexity,
            'max_nesting': max_nesting,
            'num_functions': num_functions,
        }
    
    def _extract_c_vuln_features(self, code_text):
        """Extract vulnerability features from C/C++"""
        # Buffer overflow risks
        unsafe_funcs = len(re.findall(r'\b(strcpy|strcat|sprintf|gets|scanf)\s*\(', code_text))
        
        # Format string vulnerabilities
        format_string = len(re.findall(r'printf\s*\(\s*\w+\s*\)', code_text))  # printf(var) without format
        
        # Memory leaks (malloc without free nearby)
        mallocs = len(re.findall(r'\bmalloc\s*\(', code_text))
        frees = len(re.findall(r'\bfree\s*\(', code_text))
        memory_leak_risk = 1 if mallocs > frees + 2 else 0
        
        # Command injection
        cmd_injection = int('system(' in code_text or 'popen(' in code_text or 'exec' in code_text)
        
        # Hardcoded credentials
        hardcoded = len(re.findall(r'(password|secret|key)\s*\[\s*\]\s*=\s*"[^"]{8,}"', code_text, re.IGNORECASE))
        
        return {
            'sql_injection': 0,
            'eval_exec': 0,
            'hardcoded_secrets': hardcoded,
            'command_injection': cmd_injection,
            'buffer_overflow': unsafe_funcs,
            'format_string': format_string,
            'memory_leak_risk': memory_leak_risk,
            'total_signals': 0
        }
    
    # ==================== JavaScript/TypeScript ====================
    def _extract_js_bug_features(self, code_text):
        """Extract bug-related features from JS/TS"""
        # Count functions
        num_functions = len(re.findall(r'(function\s+\w+|const\s+\w+\s*=\s*(\([^)]*\)|async)?\s*=>|\w+\s*\([^)]*\)\s*\{)', code_text))
        
        # Estimate complexity
        decision_keywords = len(re.findall(r'\b(if|else|for|while|switch|case|catch|&&|\|\||\?|\.then|\.catch)\b', code_text))
        max_complexity = min(decision_keywords // max(num_functions, 1) + 1, 50)
        
        max_nesting = self._calculate_nesting_generic(code_text, 'javascript')
        
        return {
            'avg_complexity': round(decision_keywords / max(num_functions, 1), 2),
            'max_complexity': max_complexity,
            'max_nesting': max_nesting,
            'num_functions': num_functions,
        }
    
    def _extract_js_vuln_features(self, code_text):
        """Extract vulnerability features from JS/TS"""
        # XSS via innerHTML
        xss_risk = len(re.findall(r'\.innerHTML\s*=', code_text))
        xss_risk += len(re.findall(r'dangerouslySetInnerHTML', code_text))
        
        # eval usage
        eval_usage = int('eval(' in code_text or 'Function(' in code_text or 'setTimeout(' in code_text and '"' in code_text)
        
        # SQL injection (if using raw queries)
        sql_injection = len(re.findall(r'(query|execute)\s*\(\s*[`"\'].*\$\{', code_text))
        sql_injection += len(re.findall(r'["\'].*SELECT.*["\'].*\+', code_text, re.IGNORECASE))
        
        # Hardcoded secrets - enhanced patterns for API keys
        # Note: [^\n"\']{8,} prevents matching across line boundaries
        secret_patterns = [
            r'(password|secret|apiKey|token|API_KEY|auth)\s*[=:]\s*["\'][^\n"\']{8,}["\']',  # Generic secrets (single line)
            r'AIzaSy[a-zA-Z0-9_-]{33}',  # Google API keys
            r'sk_live_[a-zA-Z0-9]{24,}',  # Stripe live keys
            r'sk_test_[a-zA-Z0-9]{24,}',  # Stripe test keys
            r'AKIA[A-Z0-9]{16}',  # AWS Access Key IDs
            r'ghp_[a-zA-Z0-9]{36}',  # GitHub personal access tokens
        ]
        hardcoded = sum(len(re.findall(p, code_text, re.IGNORECASE)) for p in secret_patterns)
        
        # Prototype pollution
        proto_pollution = int('__proto__' in code_text or 'constructor.prototype' in code_text)
        
        # Command injection (Node.js)
        cmd_injection = int('child_process' in code_text or 'exec(' in code_text or 'spawn(' in code_text)
        
        return {
            'sql_injection': sql_injection,
            'eval_exec': eval_usage,
            'hardcoded_secrets': hardcoded,
            'command_injection': cmd_injection,
            'xss_risk': xss_risk,
            'prototype_pollution': proto_pollution,
            'total_signals': 0
        }
    
    # ==================== GENERIC ====================
    def _calculate_nesting_generic(self, code_text, language):
        """Calculate nesting depth by counting braces/indentation"""
        max_depth = 0
        current_depth = 0
        
        for char in code_text:
            if char == '{':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == '}':
                current_depth = max(0, current_depth - 1)
        
        return max_depth
    
    def _generic_bug_features(self, code_text):
        """Generic bug feature extraction"""
        return {
            'avg_complexity': 0,
            'max_complexity': 0,
            'max_nesting': self._calculate_nesting_generic(code_text, 'generic'),
            'num_functions': 0,
        }
    
    def _generic_vuln_features(self, code_text):
        """Generic vulnerability detection"""
        return {
            'sql_injection': 0,
            'eval_exec': 0,
            'hardcoded_secrets': len(re.findall(r'(password|secret|api_key)\s*=\s*["\'][^"\']{8,}["\']', code_text, re.IGNORECASE)),
            'command_injection': 0,
            'total_signals': 0
        }
    
    def _default_features(self, filepath, language):
        """Return default features for unsupported files"""
        return {
            'bug_features': {
                'avg_complexity': 0,
                'max_complexity': 0,
                'max_nesting': 0,
                'num_functions': 0,
                'lines_of_code': 0,
                'language': language
            },
            'vulnerability_features': {
                'sql_injection': 0,
                'eval_exec': 0,
                'hardcoded_secrets': 0,
                'command_injection': 0,
                'total_signals': 0
            },
            'filepath': filepath,
            'language': language
        }


def calculate_total_signals(vuln_features):
    """Calculate total vulnerability signals"""
    total = 0
    for key, value in vuln_features.items():
        if key != 'total_signals' and isinstance(value, (int, float)):
            total += value
    vuln_features['total_signals'] = total
    return total
