import pytest

from api_requests.requests import GetBooking
from utils.helpers import write_booking_detail, read_generated_ids


def get_booking(booking_id):
    response = GetBooking(booking_id)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    booking = response.json()

    assert isinstance(booking, dict), "Response should be a JSON object"
    assert "firstname" in booking, "'firstname' field missing"
    assert isinstance(booking["firstname"], str), "'firstname' should be a string"
    assert "lastname" in booking, "'lastname' field missing"
    assert isinstance(booking["lastname"], str), "'lastname' should be a string"
    assert "totalprice" in booking, "'totalprice' field missing"
    assert isinstance(booking["totalprice"], int), "'totalprice' should be an integer"
    assert "depositpaid" in booking, "'depositpaid' field missing"
    assert isinstance(booking["depositpaid"], bool), "'depositpaid' should be a boolean"
    assert "bookingdates" in booking, "'bookingdates' field missing"
    bookingdates = booking["bookingdates"]
    assert isinstance(bookingdates, dict), "'bookingdates' should be an object"
    assert "checkin" in bookingdates, "'checkin' field missing in bookingdates"
    assert isinstance(bookingdates["checkin"], str), "'checkin' should be a string"
    assert "checkout" in bookingdates, "'checkout' field missing in bookingdates"
    assert isinstance(bookingdates["checkout"], str), "'checkout' should be a string"
    assert "additionalneeds" in booking, "'additionalneeds' field missing"
    assert isinstance(booking["additionalneeds"], str), "'additionalneeds' should be a string"

    write_booking_detail(booking_id, booking, prefix="find_")
    return booking

@pytest.mark.order(6)
def test_get_booking():
    data = read_generated_ids()

    booking_ids_date = data.get("date_filtered", [])
    if booking_ids_date:
        booking_id_date = booking_ids_date[0]
        get_booking(booking_id_date)
    else:
        print("Warning: 'date_filtered' list is empty, skipping related booking test.")

    booking_ids_name = data.get("name_filtered", [])
    if booking_ids_name:
        booking_id_name = booking_ids_name[0]
        get_booking(booking_id_name)
    else:
        print("Warning: 'name_filtered' list is empty, skipping related booking test.")

