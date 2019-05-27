from geopy import distance


def calculate_distance(last_trip, current_waypoint):
    response = distance.distance(
        (current_waypoint.lat, current_waypoint.lng), (last_trip.lat, last_trip.lng)
    ).meters
    return int(round(response))
