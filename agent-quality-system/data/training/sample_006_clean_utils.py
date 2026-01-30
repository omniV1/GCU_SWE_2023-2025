# sample_006_clean_utils.py - Clean utility functions, should PASS all gates

def format_date(date_obj, format_str="%Y-%m-%d"):
    """Format a date object to string"""
    return date_obj.strftime(format_str)

def parse_json(json_string):
    """Safely parse JSON string"""
    import json
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        return None

def validate_email(email):
    """Basic email validation"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def truncate_string(text, max_length=100):
    """Truncate string to maximum length"""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."
