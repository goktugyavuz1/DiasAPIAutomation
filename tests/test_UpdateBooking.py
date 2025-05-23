import pytest

from api_requests.requests import UpdateBooking
from tests.test_GetBooking import get_booking
from utils.helpers import get_booking_field
import tests.test_data as td

@pytest.mark.order(8)
def test_update_booking(created_booking_id, auth_token):

    firstname = td.UPDATED_FIRSTNAME
    lastname = td.UPDATED_LASTNAME
    totalprice = td.UPDATED_TOTALPRICE
    depositpaid = td.UPDATED_DEPOSITPAID
    checkin = td.UPDATED_CHECKIN
    checkout = td.UPDATED_CHECKOUT
    additionalneeds = td.UPDATED_ADDITIONALNEEDS

    response = UpdateBooking(
        created_booking_id,
        firstname,
        lastname,
        totalprice,
        depositpaid,
        checkin,
        checkout,
        additionalneeds,
        auth_token
    )
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    data = response.json()
    assert data["firstname"] == firstname, "Firstname mismatch"
    assert data["lastname"] == lastname, "Lastname mismatch"
    assert data["totalprice"] == totalprice, "Totalprice mismatch"
    assert data["depositpaid"] == depositpaid, "Depositpaid mismatch"
    assert data["bookingdates"]["checkin"] == checkin, "Checkin date mismatch"
    assert data["bookingdates"]["checkout"] == checkout, "Checkout date mismatch"
    assert data["additionalneeds"] == additionalneeds, "Additionalneeds mismatch"

    booking_id = created_booking_id

    get_booking(booking_id)
    assert get_booking_field(booking_id, "firstname") == firstname, f"Expected firstname '{get_booking_field(booking_id, "firstname")}', but got '{firstname}'"
    assert get_booking_field(booking_id, "lastname") == lastname, f"Expected lastname '{get_booking_field(booking_id, "lastname")}', but got '{lastname}'"
    assert get_booking_field(booking_id, "totalprice") == totalprice, f"Expected totalprice '{get_booking_field(booking_id, "totalprice")}', but got '{totalprice}'"
    assert get_booking_field(booking_id, "depositpaid") == depositpaid, f"Expected depositpaid '{get_booking_field(depositpaid, "depositpaid")}', but got '{depositpaid}'"
    assert get_booking_field(booking_id, "bookingdates",
                             "checkin") == checkin, f"Expected checkin '{get_booking_field(booking_id, 'bookingdates', 'checkin')}', but got '{checkin}'"
    assert get_booking_field(booking_id, "bookingdates",
                             "checkout") == checkout, f"Expected checkout '{get_booking_field(booking_id, 'bookingdates', 'checkout')}', but got '{checkout}'"




