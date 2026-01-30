# sample_005_eval.py - Dangerous eval usage, should FAIL vuln gate

def execute_user_code(user_input):
    """Dangerous use of eval"""
    result = eval(user_input)
    return result

def dynamic_import(module_name):
    """Dangerous use of exec"""
    exec(f"import {module_name}")
