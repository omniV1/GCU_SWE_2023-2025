# sample_010_both_issues.py - Both complexity AND vulnerability issues, should FAIL both gates

def dangerous_complex_function(user_input, config, db_connection, options, flags):
    """This function has multiple issues: high complexity AND security vulnerabilities"""
    results = []
    
    # SQL injection vulnerability
    query = "SELECT * FROM users WHERE name = " + user_input
    
    if config is not None:
        if config.get('enabled'):
            if options['mode'] == 'advanced':
                if flags['verbose']:
                    if flags['debug']:
                        for i in range(100):
                            for j in range(100):
                                if i > j:
                                    # Hardcoded secret
                                    api_key = "secret_key_123456789"
                                    results.append({
                                        'i': i,
                                        'j': j,
                                        'key': api_key
                                    })
    
    # Dangerous eval
    result = eval(user_input)
    
    return results
