# sample_009_pickle_vuln.py - Pickle deserialization vulnerability, should FAIL vuln gate

import pickle

def load_user_data(data_bytes):
    """Dangerous: deserializes untrusted pickle data"""
    user_data = pickle.loads(data_bytes)
    return user_data

def load_from_file(filepath):
    """Dangerous: loads pickle from file without validation"""
    with open(filepath, 'rb') as f:
        return pickle.loads(f.read())

def process_cached_data(cache_key, data_bytes):
    """Processes cached data unsafely"""
    data = pickle.loads(data_bytes)
    return data.get(cache_key)
