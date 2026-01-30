# sample_014_clean_math.py - Clean math utilities, should PASS all gates

def calculate_average(numbers):
    """Calculate average of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    """Calculate standard deviation"""
    if len(numbers) < 2:
        return 0
    
    avg = calculate_average(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

def normalize_values(values, min_val=0, max_val=1):
    """Normalize values to a given range"""
    if not values:
        return []
    
    current_min = min(values)
    current_max = max(values)
    
    if current_max == current_min:
        return [min_val] * len(values)
    
    scale = (max_val - min_val) / (current_max - current_min)
    return [(v - current_min) * scale + min_val for v in values]

def clamp(value, minimum, maximum):
    """Clamp value between minimum and maximum"""
    return max(minimum, min(value, maximum))
