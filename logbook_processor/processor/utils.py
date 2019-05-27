from datetime import datetime

import simplejson as json
from geopy import distance
from logbook_processor.processor.processor import Waypoint


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


def get_waypoints_from_json(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    waypoints = [Waypoint(**waypoint) for waypoint in data]
    return waypoints


def save_trips(file_path, trip_list):
    json_trip = json.dumps(trip_list, indent=2, namedtuple_as_object=True)
    with open(file_path, "w") as writer:
        writer.write(json_trip)
