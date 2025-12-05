
import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    """This is a Pytest fixture that gives a shared APIClient instance for all tests
    
    Using session scope ensures the same client is used across all test functions,
    improving test performance.
    
    Returns:
        APIClient instance configured for FakeStore API
    """
    return APIClient()
