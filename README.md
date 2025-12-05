
# FakeStore API Pytest Project

## Overview
Automated test suite for the FakeStore API (https://fakestoreapi.com) covering 3 user stories and some additional API functionality testing.

## Features
- Covers all 3 user stories with tests against live API endpoints
- Tests both men's and women's clothing categories using parametrization
- Validates API responses with `jsonschema` to catch structural issues
- Tries to handle flaky network calls with automatic retry logic
- Cleans up test data (carts/products) after each run
- Includes negative test cases for edge scenarios
- Test markers for selective execution (`quick_regression`, `full_regression`)
- Some tests stubbed for future implementation (marked with `@pytest.mark.skip`)

## Setup
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running Tests
```bash
# Run all active tests
pytest -v

# Run only the 3 user story tests (fast)
pytest -m quick_regression -v

# Run full regression suite
pytest -m full_regression -v

# Run with coverage report
pytest --cov=. --cov-report=html
```

