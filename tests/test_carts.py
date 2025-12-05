
import pytest
from datetime import datetime

@pytest.mark.full_regression
def test_get_all_carts(api_client):
    """
    Test: Retrieve all shopping carts from the store
    
    Validates that the API returns a list of carts with proper structure.
    """
    response = api_client.get("/carts")
    assert response.status_code == 200
    
    carts = response.json()
    assert isinstance(carts, list), "Should return a list of carts"
    assert len(carts) > 0, "Should have at least one cart"
    
    # Validate cart structure
    cart = carts[0]
    assert 'id' in cart, "Cart should have an ID"
    assert 'userId' in cart, "Cart should have a userId"
    assert 'date' in cart, "Cart should have a date"
    assert 'products' in cart, "Cart should have products list"
    assert isinstance(cart['products'], list), "Products should be a list"

