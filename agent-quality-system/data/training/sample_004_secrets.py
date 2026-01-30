# sample_004_secrets.py - Hardcoded secrets, should FAIL vuln gate

API_KEY = "sk_live_abc123def456ghi789"
DATABASE_PASSWORD = "super_secret_password_123"

def connect_to_api():
    """Connects using hardcoded API key"""
    headers = {'Authorization': f'Bearer {API_KEY}'}
    return make_request(headers)
