# sample_012_high_nesting.py - Very high nesting depth, should FAIL bug gate

def deeply_nested_logic(data, filters, validators, processors, outputters):
    """Extremely nested function that is hard to maintain"""
    results = []
    
    if data:
        for item in data:
            if filters.get('active'):
                if item.get('valid'):
                    for validator in validators:
                        if validator.check(item):
                            for processor in processors:
                                if processor.can_handle(item):
                                    for outputter in outputters:
                                        if outputter.accepts(item):
                                            processed = processor.process(item)
                                            results.append(outputter.output(processed))
    
    return results
