#USER STORY 1 - discuss Quantity issue 
import pytest
from utils.data_helpers import find_cheapest, generate_cart_payload
from jsonschema import validate

# JSON schema to validate product structure returned by the API
product_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "price": {"type": "number"},
        "category": {"type": "string"}
    },
    "required": ["id", "title", "price", "category"]
}

@pytest.mark.quick_regression
@pytest.mark.full_regression
def test_add_cheapest_electronic_to_cart(api_client):
    """
    User Story 1: As an online shopper, I want to view all available products 
    and add the cheapest electronics item to my cart.
    
    Acceptance Criteria:
    - The product must belong to a specific category (electronics)
    - Only products that are in stock should be considered (NOTE: FakeStore API 
      doesn't provide inventory/stock data, so this cannot be validated)
    - Once added to cart, the product should appear with correct price and quantity
    """
    # Step 1: Retrieve all electronics products from the category endpoint
    response = api_client.get("/products/category/electronics")
    assert response.status_code == 200
    electronics = response.json()
    assert len(electronics) > 0, "No electronics found"

    # Step 2: Validate that products has the correct schema
    validate(instance=electronics[0], schema=product_schema)

    # Step 3: Find the cheapest electronics product
    cheapest = find_cheapest(electronics)
    
    # Step 4: Create cart payload and add the cheapest product to cart
    cart_payload = generate_cart_payload(cheapest['id'])
    cart_response = api_client.post("/carts", cart_payload)
    assert cart_response.status_code in [200, 201], "Cart creation should return 200 or 201"
    cart = cart_response.json()

    # Step 5: Verify the product was added with correct ID and quantity
    added_product = cart['products'][0]
    assert added_product['productId'] == cheapest['id'], "Product ID mismatch in cart"
    assert added_product['quantity'] == 1, "Quantity should be 1"

    # Cleanup: Remove the test cart (what we would do in a prod scenario where data would persist)
    api_client.delete(f"/carts/{cart['id']}")
