import pytest

from api_requests.requests import GetBookingIds
from utils.helpers import read_generated_ids, write_generated_ids
import tests.test_data as td

def _save_ids(key, ids):
    try:
        data = read_generated_ids()
    except FileNotFoundError:
        data = {}
    data[key] = ids
    write_generated_ids(data)

@pytest.mark.order(3)
def test_get_booking_ids_all():
    response = GetBookingIds()
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    booking_ids = response.json()
    assert isinstance(booking_ids, list), "Response should be a list"
    if not booking_ids:
        print("Warning: 'all_ids' list returned empty.")
    else:
        for item in booking_ids:
            assert "bookingid" in item, "Each item should have 'bookingid' key"
        ids = [item["bookingid"] for item in booking_ids]
        _save_ids("all_ids", ids)

@pytest.mark.order(4)
def test_get_booking_ids_filter_name():
    response = GetBookingIds(firstname=td.FILTER_FIRSTNAME, lastname=td.FILTER_LASTNAME)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    booking_ids = response.json()
    assert isinstance(booking_ids, list), "Response should be a list"
    if not booking_ids:
        print("Warning: 'name_filtered' list returned empty.")
    else:
        for item in booking_ids:
            assert "bookingid" in item, "Each item should have 'bookingid' key"
        ids = [item["bookingid"] for item in booking_ids]
        _save_ids("name_filtered", ids)

@pytest.mark.order(5)
def test_get_booking_ids_filter_dates():
    response = GetBookingIds(checkin=td.FILTER_CHECKIN, checkout=td.FILTER_CHECKOUT)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    booking_ids = response.json()
    assert isinstance(booking_ids, list), "Response should be a list"
    if not booking_ids:
        print("Warning: 'date_filtered' list returned empty.")
    else:
        for item in booking_ids:
            assert "bookingid" in item, "Each item should have 'bookingid' key"
        ids = [item["bookingid"] for item in booking_ids]
        _save_ids("date_filtered", ids)
