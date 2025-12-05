
import pytest
from tests.test_constants import AUTH_VALID_USERNAME, AUTH_VALID_PASSWORD

@pytest.mark.full_regression
def test_successful_login(api_client):
    """
    Test: Authenticate user and receive JWT token
    
    Validates that valid credentials return a JWT token for authentication.
    According to FakeStore API docs, use any existing user credentials.
    """
    login_credentials = {
        "username": AUTH_VALID_USERNAME,
        "password": AUTH_VALID_PASSWORD
    }
    
    response = api_client.post("/auth/login", login_credentials)
    assert response.status_code in [200, 201], "Login should return 200 or 201"
    
    auth_response = response.json()
    assert 'token' in auth_response, "Login should return a token"
    
    # Validate JWT token format (should have 3 parts separated by dots)
    token = auth_response['token']
    assert isinstance(token, str), "Token should be a string"
    assert len(token) > 0, "Token should not be empty"
    
    # Basic JWT format validation (header.payload.signature)
    token_parts = token.split('.')
    assert len(token_parts) == 3, "JWT should have 3 parts separated by dots"


@pytest.mark.negative
@pytest.mark.full_regression
def test_login_with_invalid_username(api_client):
    """
    Negative Test: Attempt login with non-existent username
    
    Should reject authentication with invalid credentials.
    Note: FakeStore API returns 401 for authentication failures.
    """
    invalid_credentials = {
        "username": "somethingsomethingdarkside1234",
        "password": "protec"
    }
    
    response = api_client.post("/auth/login", invalid_credentials)
    assert response.status_code == 401, \
        "Invalid credentials should return 401 Unauthorized"

@pytest.mark.skip(reason="TODO: Implement later")
@pytest.mark.negative
@pytest.mark.full_regression
def test_login_with_wrong_password(api_client):
    """
    Negative Test: Attempt login with incorrect password
    
    Should reject authentication when password doesn't match.
    """
    pass

@pytest.mark.skip(reason="TODO: Implement later")
@pytest.mark.negative
@pytest.mark.full_regression
def test_login_with_missing_fields(api_client):
    """
    Negative Test: Attempt login with incomplete credentials
    
    Should validate that both username and password are required.
    """
    pass


