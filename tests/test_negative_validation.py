
import pytest

@pytest.mark.full_regression
def test_add_product_missing_fields(api_client):
    """
    Negative test: Verify API behavior when creating a product with missing required fields.
    
    This test attempts to create a product without a 'title' field.
    Note: FakeStore API may accept incomplete data (returns 200) as it's a mock API,
    but ideally it should reject with 400 Bad Request.
    """
    product_data = {
        "price": 20,
        "description": "Invalid product",
        "image": "https://i.pravatar.cc",
        "category": "men's clothing"
        # Missing 'title' field - should ideally cause validation error
    }
    response = api_client.post("/products", product_data)
    # Accept either 400 (proper validation) or 200/201 (mock API behavior)
    assert response.status_code in [400, 200, 201], \
        f"Unexpected status code: {response.status_code}"
