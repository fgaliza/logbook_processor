import os

import pytest
from logbook_processor.processor.processor import Trip, Waypoint
from logbook_processor.processor.utils import (
    calculate_distance,
    calculate_minute_difference,
    get_waypoints_from_json,
    save_trips,
)


def get_waypoint_distance(lat, lng):
    return Waypoint(lat=lat, timestamp="2019-05-23T00:00:00Z", lng=lng)


def test_calculate_distance_with_no_movement():
    pointA = get_waypoint_distance(lat=1, lng=1)
    pointB = get_waypoint_distance(lat=1, lng=1)
    response = calculate_distance(pointA, pointB)
    assert response == 0


def test_calculate_distance():
    pointA = get_waypoint_distance(lat=1, lng=1)
    pointB = get_waypoint_distance(lat=2, lng=2)
    response = calculate_distance(pointA, pointB)
    assert response == 156876  # response in meters


def test_calculate_minute_difference():
    response = calculate_minute_difference(start="2019-05-23T00:00:00Z", end="2019-05-23T00:05:00Z")
    assert response == 5


def test_calculate_minute_difference_same_timestamp():
    response = calculate_minute_difference(start="2019-05-23T00:00:00Z", end="2019-05-23T00:00:00Z")
    assert response == 0


def test_calculate_minute_difference_invalid_timestamp():
    with pytest.raises(ValueError):
        calculate_minute_difference(start="abc", end="abc")


def test_get_waypoints_from_json():
    waypoints = get_waypoints_from_json(file_path="logbook_processor/data/waypoints.json")
    assert len(waypoints) == 175
    assert type(waypoints) == list
    assert all(type(waypoint) == Waypoint for waypoint in waypoints)


def test_get_waypoints_from_json_invalid_path():
    with pytest.raises(FileNotFoundError):
        get_waypoints_from_json(file_path="abc/abc.py")


def test_save_trips():
    start = get_waypoint_distance(1, 1)
    end = get_waypoint_distance(2, 2)
    trip = Trip(start=start, end=end, distance=156876)
    file_path = "logbook_processor/data/test.json"
    save_trips(file_path=file_path, trip_list=[trip])
    assert os.path.exists(file_path)
    os.remove(file_path)
