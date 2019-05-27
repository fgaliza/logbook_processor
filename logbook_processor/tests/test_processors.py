from logbook_processor.processor.entities import Trip, Waypoint
from logbook_processor.processor.processors import LogbookListProcessor


def get_logbook_response(waypointA, waypointB):
    logbook_list_processor = LogbookListProcessor((waypointA, waypointB))
    return logbook_list_processor.get_trips()


def test_logbook_list_processor_no_last_trip():
    waypoint = Waypoint(lat=1, timestamp="2019-05-23T00:00:00Z", lng=1)
    logbook_list_processor = LogbookListProcessor((waypoint,))
    response = logbook_list_processor.get_trips()
    assert response is ()


def test_logbook_list_processor_distance_smaller_than_fifteen():
    waypointA = Waypoint(lat=1, timestamp="2019-05-23T00:00:00Z", lng=1)
    waypointB = Waypoint(lat=1.000001, timestamp="2019-05-23T10:00:00Z", lng=1)
    response = get_logbook_response(waypointA, waypointB)
    assert response is ()


def test_logbook_list_processor_time_difference_smaller_than_three():
    waypointA = Waypoint(lat=1, timestamp="2019-05-23T00:00:00Z", lng=1)
    waypointB = Waypoint(lat=2, timestamp="2019-05-23T00:02:59Z", lng=2)
    response = get_logbook_response(waypointA, waypointB)
    assert response is ()


def test_logbook_list_processor_return_trip():
    waypointA = Waypoint(lat=1, timestamp="2019-05-23T00:00:00Z", lng=1)
    waypointB = Waypoint(lat=2, timestamp="2019-05-23T10:02:59Z", lng=2)
    response = get_logbook_response(waypointA, waypointB)
    assert len(response) == 1
    assert type(response[0]) is Trip
    assert response[0].start is waypointA
    assert response[0].end is waypointB
    assert response[0].distance == 156876
