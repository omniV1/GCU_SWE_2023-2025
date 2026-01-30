# sample_015_multiple_vulns.py - Multiple vulnerability types, should FAIL vuln gate

import os
import pickle

# Hardcoded credentials
DB_PASSWORD = "production_password_xyz789"
API_TOKEN = "token_abcdef123456789"

def process_user_input(user_code, data_bytes):
    """Multiple vulnerabilities in one function"""
    # Eval vulnerability
    result = eval(user_code)
    
    # Pickle vulnerability  
    data = pickle.loads(data_bytes)
    
    # Command injection
    os.system(f"echo {result}")
    
    return data

def execute_script(script_path):
    """Dangerous exec usage"""
    with open(script_path, 'r') as f:
        exec(f.read())
