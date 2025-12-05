
import pytest

@pytest.mark.full_regression
def test_get_all_users(api_client):
    """
    Test: Retrieve all users from the system
    
    Validates that the API returns a list of users with complete profile data.
    """
    response = api_client.get("/users")
    assert response.status_code == 200
    
    users = response.json()
    assert isinstance(users, list), "Should return a list of users"
    assert len(users) > 0, "Should have at least one user"
    
    # Validate user structure
    user = users[0]
    assert 'id' in user
    assert 'email' in user
    assert 'username' in user
    assert 'name' in user
    assert 'address' in user
    assert 'phone' in user


@pytest.mark.skip(reason="TODO: Implement later")
@pytest.mark.full_regression
def test_create_new_user(api_client):
    """
    Test: Create a new user with complete profile information
    
    Validates that all user fields can be set during creation.
    """
    pass


@pytest.mark.skip(reason="TODO: Implement later")
@pytest.mark.full_regression
def test_create_user(api_client):
    """
    Test: Update user profile information
    
    Validates that user details can be modified.
    """
    pass


@pytest.mark.skip(reason="TODO: Implement later")
@pytest.mark.full_regression
def test_delete_user(api_client):
    """
    Test: Delete a user from the system
    
    Validates that users can be removed successfully.
    """
    pass

