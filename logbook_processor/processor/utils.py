from datetime import datetime

from geopy import distance


def calculate_distance(last_trip, current_waypoint):
    response = distance.distance(
        (current_waypoint.lat, current_waypoint.lng), (last_trip.lat, last_trip.lng)
    ).meters
    return int(round(response))


def calculate_minute_difference(start, end):
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    new_timestamp = datetime.strptime(end, fmt)
    last_timestamp = datetime.strptime(start, fmt)
    delta = new_timestamp - last_timestamp
    minutes = int(delta.total_seconds() / 60)
    return minutes
