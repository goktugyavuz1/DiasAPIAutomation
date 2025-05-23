import os
from datetime import datetime
import pytest
from api_requests.requests import get_token
from tests.test_CreateBooking import test_create_booking

@pytest.fixture(scope="session")
def auth_token():
    status, token = get_token()
    if status != 200 or not token:
        pytest.skip("Auth token could not be retrieved")
    return token

@pytest.fixture(scope="session")
def created_booking_id():
    booking_id = test_create_booking()
    return booking_id

def pytest_configure(config):
    reports_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = os.path.join(reports_dir, f"report_{timestamp}.html")

    config.option.htmlpath = report_path
    config.option.self_contained_html = True
