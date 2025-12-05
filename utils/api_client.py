
import requests
import time

BASE_URL = "https://fakestoreapi.com"

class APIClient:
    """Wrapper for FakeStore API with retry logic for handling flaky failures and stops us from repeating URLs everywhere"""

    def _request_with_retry(self, method, url, **kwargs):
        """Execute HTTP request with retry logic for server errors 
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            url: Full URL to request
            **kwargs: Additional arguments to pass to requests.request()
            
        Returns:
            Response object from the successful request or last attempt
        """
        retries = 3
        for attempt in range(retries):
            response = requests.request(method, url, **kwargs)
            # Only retry on server errors (5xx), client errors (4xx) are returned instantly as there's no point in waiting
            if response.status_code < 500:
                return response
            time.sleep(2)  # Wait 2 seconds before retry to handle transient failures
        return response

    def get(self, endpoint):
        """Send GET request to the specified endpoint"""
        return self._request_with_retry("GET", f"{BASE_URL}{endpoint}")

    def post(self, endpoint, data):
        """Send POST request with JSON payload to the specified endpoint"""
        return self._request_with_retry("POST", f"{BASE_URL}{endpoint}", json=data)

    def put(self, endpoint, data):
        """Send PUT request with JSON payload to the specified endpoint"""
        return self._request_with_retry("PUT", f"{BASE_URL}{endpoint}", json=data)

    def delete(self, endpoint):
        """Send DELETE request to the specified endpoint"""
        return self._request_with_retry("DELETE", f"{BASE_URL}{endpoint}")

    def patch(self, endpoint, data):
        """Send PATCH request with JSON payload to the specified endpoint"""
        return self._request_with_retry("PATCH", f"{BASE_URL}{endpoint}", json=data)
