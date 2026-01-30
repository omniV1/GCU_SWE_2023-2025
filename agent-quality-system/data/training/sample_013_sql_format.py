# sample_013_sql_format.py - SQL injection via format strings, should FAIL vuln gate

def search_users(search_term, sort_field):
    """SQL injection via .format()"""
    query = "SELECT * FROM users WHERE name LIKE '%{}%' ORDER BY {}".format(
        search_term, sort_field
    )
    return execute_query(query)

def get_filtered_products(category, min_price):
    """Another format string SQL injection"""
    query = "SELECT * FROM products WHERE category = '{}' AND price > {}".format(
        category, min_price
    )
    return execute_query(query)
