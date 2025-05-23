import pytest

from api_requests.requests import get_token

@pytest.mark.order(2)
def test_get_token_success():
    status_code, token = get_token()
    assert status_code == 200, f"Expected status code 200 but got {status_code}"
    assert token is not None, "Token should not be None"
    assert isinstance(token, str), "Token should be a string"
    assert len(token) > 0, "Token should not be empty"
