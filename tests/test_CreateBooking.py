import pytest

from api_requests.requests import CreateBooking
from tests.test_GetBooking import get_booking
from utils.helpers import  get_booking_field
import tests.test_data as td

@pytest.mark.order(7)
def test_create_booking():
    firstname = td.CREATED_FIRSTNAME
    lastname = td.CREATED_LASTNAME
    totalprice = td.CREATED_TOTALPRICE
    depositpaid = td.CREATED_DEPOSITPAID
    checkin = td.CREATED_CHECKIN
    checkout = td.CREATED_CHECKOUT
    additionalneeds = td.CREATED_ADDITIONALNEEDS

    response = CreateBooking(firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    data = response.json()
    assert "bookingid" in data, "'bookingid' missing in response"
    assert "booking" in data, "'booking' object missing in response"
    booking = data["booking"]
    assert booking["firstname"] == firstname, "Firstname mismatch"
    assert booking["lastname"] == lastname, "Lastname mismatch"
    assert booking["totalprice"] == totalprice, "Totalprice mismatch"
    assert booking["depositpaid"] == depositpaid, "Depositpaid mismatch"
    assert booking["bookingdates"]["checkin"] == checkin, "Checkin date mismatch"
    assert booking["bookingdates"]["checkout"] == checkout, "Checkout date mismatch"
    assert booking["additionalneeds"] == additionalneeds, "Additionalneeds mismatch"

    booking_id = data["bookingid"]

    get_booking(booking_id)
    assert get_booking_field(booking_id, "firstname") == firstname, f"Expected firstname '{get_booking_field(booking_id, "firstname")}', but got '{firstname}'"
    assert get_booking_field(booking_id, "lastname") == lastname, f"Expected lastname '{get_booking_field(booking_id, "lastname")}', but got '{lastname}'"
    assert get_booking_field(booking_id, "totalprice") == totalprice, f"Expected totalprice '{get_booking_field(booking_id, "totalprice")}', but got '{totalprice}'"
    assert get_booking_field(booking_id, "depositpaid") == depositpaid, f"Expected depositpaid '{get_booking_field(depositpaid, "depositpaid")}', but got '{depositpaid}'"
    assert get_booking_field(booking_id, "bookingdates",
                             "checkin") == checkin, f"Expected checkin '{get_booking_field(booking_id, 'bookingdates', 'checkin')}', but got '{checkin}'"
    assert get_booking_field(booking_id, "bookingdates",
                             "checkout") == checkout, f"Expected checkout '{get_booking_field(booking_id, 'bookingdates', 'checkout')}', but got '{checkout}'"

    return booking_id