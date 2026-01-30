
# Demo code with various quality issues

import os
import pickle

API_KEY = "FAKE_SECRET_KEY_12345_DEMO_ONLY"  # Hardcoded secret!

def complex_function(data, config, options):
    """Function with high complexity and nesting"""
    if data:
        if config.get('enabled'):
            if options.get('mode') == 'advanced':
                for item in data:
                    for sub in item:
                        if sub.get('valid'):
                            # SQL injection vulnerability
                            query = "SELECT * FROM users WHERE id = " + str(sub['id'])
                            
                            # Command injection
                            os.system("process " + sub['name'])
                            
                            # Insecure deserialization
                            result = pickle.loads(sub['data'])
                            
                            # Dangerous eval
                            eval(sub['expression'])
    return True

# Duplicate code block 1
def process_a(x):
    result = x * 2
    result = result + 10
    result = result / 5
    return result

# Duplicate code block 2
def process_b(x):
    result = x * 2
    result = result + 10
    result = result / 5
    return result
