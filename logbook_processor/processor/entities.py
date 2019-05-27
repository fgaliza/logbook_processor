from datetime import datetime
from typing import NamedTuple


class Waypoint(NamedTuple):
    timestamp: datetime
    lat: float
    lng: float


class Trip(NamedTuple):
    start: Waypoint
    end: Waypoint
    distance: int
