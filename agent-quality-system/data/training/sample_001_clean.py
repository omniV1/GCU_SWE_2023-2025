# sample_001_clean.py - Clean code, should PASS all gates

def calculate_sum(numbers):
    """Calculate sum of a list of numbers"""
    return sum(numbers)

def find_maximum(numbers):
    """Find maximum value in list"""
    if not numbers:
        return None
    return max(numbers)

def is_even(number):
    """Check if number is even"""
    return number % 2 == 0
