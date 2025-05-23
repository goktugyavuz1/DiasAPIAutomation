import requests
import config

def get_token():
    url = f"{config.BASE_URL}/auth"
    payload = {"username": config.USERNAME, "password": config.PASSWORD}
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        return response.status_code, None
    token = response.json().get("token")
    return response.status_code, token

def GetBookingIds(firstname=None, lastname=None, checkin=None, checkout=None):
    url = f"{config.BASE_URL}/booking"
    params = {}
    if firstname:
        params["firstname"] = firstname
    if lastname:
        params["lastname"] = lastname
    if checkin:
        params["checkin"] = checkin
    if checkout:
        params["checkout"] = checkout
    response = requests.get(url, params=params)
    return response

def GetBooking(booking_id, token=None):
    url = f"{config.BASE_URL}/booking/{booking_id}"
    headers = {}
    if token:
        headers["Cookie"] = f"token={token}"
    response = requests.get(url, headers=headers)
    return response


def CreateBooking(firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
    url = f"{config.BASE_URL}/booking"
    payload = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response

def UpdateBooking(booking_id, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds, token):
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}",
    }
    payload = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }

    response = requests.put(url, json=payload, headers=headers)
    return response


def PartialUpdateBooking(booking_id, token, **kwargs):

    url = f"{config.BASE_URL}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }
    payload = kwargs
    response = requests.patch(url, json=payload, headers=headers)
    return response

def DeleteBooking(booking_id, token):
    url = f"{config.BASE_URL}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }
    response = requests.delete(url, headers=headers)
    return response
