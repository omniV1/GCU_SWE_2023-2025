# sample_008_moderate_complexity.py - Moderate complexity, should PASS bug gate

def process_order(order, user, inventory):
    """Process an order with reasonable complexity"""
    if not order or not user:
        return {"status": "error", "message": "Invalid input"}
    
    if not user.get("verified"):
        return {"status": "error", "message": "User not verified"}
    
    items_to_ship = []
    for item in order.get("items", []):
        if item["id"] in inventory:
            if inventory[item["id"]] >= item["quantity"]:
                items_to_ship.append(item)
                inventory[item["id"]] -= item["quantity"]
    
    return {
        "status": "success",
        "items": items_to_ship,
        "user_id": user["id"]
    }

def calculate_discount(total, user_tier):
    """Calculate discount based on user tier"""
    discounts = {
        "bronze": 0.05,
        "silver": 0.10,
        "gold": 0.15,
        "platinum": 0.20
    }
    return total * discounts.get(user_tier, 0)
