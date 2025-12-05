
from datetime import datetime

def find_cheapest(products):
    """Find the product with the lowest price from a list of products
    Args:
        products: List of product dictionaries containing 'price' field
    Returns:
        Product dictionary with the minimum price
    """
    return min(products, key=lambda p: p['price'])

def find_lowest_rated(products):
    """Find the product with the lowest customer rating
    Args:
        products: List of product dictionaries containing 'rating' dict with 'rate' field
        
    Returns:
        Product dictionary with the minimum rating
    """
    return min(products, key=lambda p: p['rating']['rate'])

def generate_cart_payload(product_id):
    """Generate a cart payload for adding a product to cart

    Args:
        product_id: ID of the product to add to cart
    Returns:
        Dictionary with userId, date, and products list for cart creation
    """
    return {
        "userId": 1,  # Using a fixed test user ID
        "date": datetime.now().strftime("%Y-%m-%d"),
        "products": [{"productId": product_id, "quantity": 1}]
    }
