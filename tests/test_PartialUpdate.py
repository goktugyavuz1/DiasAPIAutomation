import pytest
from api_requests.requests import PartialUpdateBooking
from tests.test_GetBooking import get_booking
from utils.helpers import get_booking_field
import tests.test_data as td


@pytest.mark.order(9)
def test_partial_update_booking(auth_token, created_booking_id):
    booking_id = created_booking_id

    new_firstname = td.NEW_FIRSTNAME
    new_lastname = td.NEW_LASTNAME

    response = PartialUpdateBooking(
        booking_id=booking_id,
        token=auth_token,
        firstname=new_firstname,
        lastname=new_lastname
    )
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    data = response.json()
    assert data.get("firstname") == new_firstname, "Firstname not updated correctly"
    assert data.get("lastname") == new_lastname, "Lastname not updated correctly"

    booking_id = created_booking_id

    get_booking(booking_id)
    assert get_booking_field(booking_id, "firstname") == new_firstname, f"Expected firstname '{get_booking_field(booking_id, "firstname")}', but got '{new_firstname}'"
    assert get_booking_field(booking_id, "lastname") == new_lastname, f"Expected lastname '{get_booking_field(booking_id, "lastname")}', but got '{new_lastname}'"
