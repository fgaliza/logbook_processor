from abc import ABCMeta, abstractmethod
from typing import Tuple, Union

from logbook_processor.processor.entities import Trip, Waypoint
from logbook_processor.processor.utils import calculate_distance, calculate_minute_difference
from progress.bar import FillingSquaresBar


class ListProcessor(metaclass=ABCMeta):
    def __init__(self, waypoints: Tuple[Waypoint]):
        """
        On initialization the ListProcessor receives the full list of all
        waypoints. This list is held in memory, so the ListProcessor has access
        to the whole list of waypoints at all time during the trip extraction
        process.

        :param waypoints: Tuple[Waypoint]
        """
        self._waypoints = waypoints

    @abstractmethod
    def get_trips(self) -> Tuple[Trip]:
        """
        This function returns a list of Trips, which is derived from
        the list of waypoints, passed to the instance on initialization.
        """
        ...


class StreamProcessor(metaclass=ABCMeta):
    @abstractmethod
    def process_waypoint(self, waypoint: Waypoint) -> Union[Trip, None]:
        """
        Instead of a list of Waypoints, the StreamProcessor only receives one
        Waypoint at a time. The processor does not have access to the full list
        of waypoints.
        If the stream processor recognizes a complete trip, the processor
        returns a Trip object, otherwise it returns None.

        :param waypoint: Waypoint
        """
        ...


class LogbookListProcessor(ListProcessor):
    def __init__(self, waypoints):
        self.last_valid_waypoint = None
        self._waypoints = waypoints
        self.trips = []

    def get_trips(self) -> Tuple[Trip]:
        bar = FillingSquaresBar("Processing", max=len(self._waypoints))
        for waypoint in self._waypoints:
            bar.next()
            if not self.last_valid_waypoint:
                self.last_valid_waypoint = waypoint
                continue
            distance = calculate_distance(self.last_valid_waypoint, waypoint)
            if distance < 15:
                continue
            time_difference = calculate_minute_difference(
                self.last_valid_waypoint.timestamp, waypoint.timestamp
            )
            if time_difference <= 3:
                continue
            trip = Trip(start=self.last_valid_waypoint, end=waypoint, distance=distance)
            self.last_valid_waypoint = waypoint
            self.trips.append(trip)
        return tuple(self.trips)
