
import pytest

@pytest.mark.full_regression
def test_get_all_categories(api_client):
    """
    Test: Retrieve all available product categories
    
    Validates that the API returns a list of valid category names that can be 
    used for filtering products.
    """
    response = api_client.get("/products/categories")
    assert response.status_code == 200
    
    categories = response.json()
    assert isinstance(categories, list), "Categories should be a list"
    assert len(categories) > 0, "Should have at least one category"
    
    # Verify known categories exist
    expected_categories = ["electronics", "jewelery", "men's clothing", "women's clothing"]
    for category in expected_categories:
        assert category in categories, f"Expected category '{category}' not found"


@pytest.mark.full_regression
def test_limit_products(api_client):
    """
    Test: Limit the number of products returned using query parameter
    
    Verifies that the API respects the 'limit' query parameter to restrict
    the number of results returned. (this test only works if the API has a limit paramaeter)
    """
   

