# sample_003_sql_injection.py - SQL injection vulnerability, should FAIL vuln gate

def get_user_by_id(user_id):
    """Vulnerable to SQL injection"""
    query = "SELECT * FROM users WHERE id = " + user_id
    return execute_query(query)

def search_products(search_term):
    """Another SQL injection vulnerability"""
    query = f"SELECT * FROM products WHERE name LIKE '%{search_term}%'"
    return execute_query(query)
