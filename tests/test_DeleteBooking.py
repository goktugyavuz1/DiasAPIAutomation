import pytest
from api_requests.requests import DeleteBooking


@pytest.mark.order(10)
def test_delete_booking(auth_token, created_booking_id):
    booking_id = created_booking_id

    response = DeleteBooking(booking_id, auth_token)
    assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"

