import pytest

from logbook_processor.processor.processor import Waypoint

from logbook_processor.processor.utils import (
    calculate_distance,
    calculate_minute_difference,
)

"""
    isort:skip_file
"""


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
    response = calculate_minute_difference(
        start="2019-05-23T00:00:00Z", end="2019-05-23T00:05:00Z"
    )
    assert response == 5


def test_calculate_minute_difference_same_timestamp():
    response = calculate_minute_difference(
        start="2019-05-23T00:00:00Z", end="2019-05-23T00:00:00Z"
    )
    assert response == 0


def test_calculate_minute_difference_invalid_timestamp():
    with pytest.raises(ValueError):
        calculate_minute_difference(start="abc", end="abc")
