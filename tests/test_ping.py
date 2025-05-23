import pytest
import requests
import config

@pytest.mark.order(1)
def test_ping_status_code():
    url = f"{config.BASE_URL}/ping"
    response = requests.get(url)
    assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"
