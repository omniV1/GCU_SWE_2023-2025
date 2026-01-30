# sample_011_clean_class.py - Clean class implementation, should PASS all gates

class UserManager:
    """Clean user management class with simple methods"""
    
    def __init__(self, db_connection):
        self.db = db_connection
        self.cache = {}
    
    def get_user(self, user_id):
        """Get user by ID with caching"""
        if user_id in self.cache:
            return self.cache[user_id]
        
        user = self.db.query_user(user_id)
        if user:
            self.cache[user_id] = user
        return user
    
    def update_user(self, user_id, data):
        """Update user data"""
        result = self.db.update(user_id, data)
        if result and user_id in self.cache:
            del self.cache[user_id]
        return result
    
    def delete_user(self, user_id):
        """Delete user"""
        result = self.db.delete(user_id)
        if result and user_id in self.cache:
            del self.cache[user_id]
        return result
