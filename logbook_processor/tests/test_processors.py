import pytest
from logbook_processor.processor.entities import Trip, Waypoint
from logbook_processor.processor.processors import LogbookStreamProcessor


@pytest.fixture
def logbook_stream_processor():
    return LogbookStreamProcessor()


def test_logbook_stream_processor_no_last_trip(logbook_stream_processor):
    waypoint = Waypoint(lat=1, timestamp="2019-05-23T00:00:00Z", lng=1)
    response = logbook_stream_processor.process_waypoint(waypoint)
    assert response is None


def test_logbook_stream_processor_distance_smaller_than_fifteen(logbook_stream_processor):
    last_waypoint = Waypoint(lat=1, timestamp="2019-05-23T00:00:00Z", lng=1)
    logbook_stream_processor.last_waypoint = last_waypoint
    new_waypoint = Waypoint(lat=1.000001, timestamp="2019-05-23T10:00:00Z", lng=1)
    response = logbook_stream_processor.process_waypoint(new_waypoint)
    assert response is None


def test_logbook_stream_processor_time_difference_smaller_than_three(logbook_stream_processor):
    last_waypoint = Waypoint(lat=1, timestamp="2019-05-23T00:00:00Z", lng=1)
    logbook_stream_processor.last_waypoint = last_waypoint
    new_waypoint = Waypoint(lat=2, timestamp="2019-05-23T00:02:59Z", lng=2)
    response = logbook_stream_processor.process_waypoint(new_waypoint)
    assert response is None


def test_logbook_stream_processor_return_trip(logbook_stream_processor):
    last_waypoint = Waypoint(lat=1, timestamp="2019-05-23T00:00:00Z", lng=1)
    logbook_stream_processor.last_waypoint = last_waypoint
    new_waypoint = Waypoint(lat=2, timestamp="2019-05-23T10:02:59Z", lng=2)
    response = logbook_stream_processor.process_waypoint(new_waypoint)
    assert type(response) is Trip
    assert response.start is last_waypoint
    assert response.end is new_waypoint
    assert response.distance == 156876
