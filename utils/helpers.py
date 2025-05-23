import os
import json

def get_booking_infos_path():
    return os.path.join(os.path.dirname(__file__), '../tests/bookingInfos.json')

def read_booking_infos():
    try:
        with open(get_booking_infos_path(), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def write_booking_infos(data):
    with open(get_booking_infos_path(), 'w') as f:
        json.dump(data, f, indent=2)

def read_generated_ids():
    data = read_booking_infos()
    return data.get("generated_ids", {})

def write_generated_ids(generated_ids_data):
    data = read_booking_infos()
    data["generated_ids"] = generated_ids_data
    write_booking_infos(data)

def read_booking_details():
    data = read_booking_infos()
    return data.get("booking_details", {})

def write_booking_detail(booking_id, booking_data, prefix="find_"):
    data = read_booking_infos()
    booking_details = data.get("booking_details", {})
    key = f"{prefix}{booking_id}"
    booking_details[key] = booking_data
    data["booking_details"] = booking_details
    write_booking_infos(data)

def get_booking_field(booking_id, field_name, subfield_name=None, prefix="find_"):
    booking_details = read_booking_details()
    key = f"{prefix}{booking_id}"
    booking = booking_details.get(key, {})
    if not booking:
        return None
    if subfield_name:
        return booking.get(field_name, {}).get(subfield_name)
    return booking.get(field_name)


