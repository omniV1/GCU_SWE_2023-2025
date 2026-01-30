# sample_002_complex.py - High complexity, should FAIL bug gate

def overly_complex_processor(data, config, options, flags, params):
    """Overly complex function with deep nesting"""
    results = []
    
    if data is not None:
        if config.get('enabled'):
            if options['mode'] == 'advanced':
                if flags['verbose']:
                    if params['level'] > 5:
                        for item in data:
                            for sub_item in item:
                                for detail in sub_item:
                                    if detail['valid']:
                                        results.append(detail['value'])
    
    return results
