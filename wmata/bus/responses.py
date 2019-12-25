"""MetroBus Responses from the WMATA API
"""
from typing import List, Optional, Dict, Any
from datetime import datetime
from .route import Route
from .stop import Stop
from ..responses import Response
from ..date import string_to_datetime

class BusPosition(Response):
    date_time: datetime
    deviation: float
    direction_number: int
    direction_text: str
    latitude: float
    longitude: float
    route: Route
    trip_end_time: datetime
    trip_id: str
    trip_start_time: datetime
    vehicle_id: str

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.date_time = string_to_datetime(json["DateTime"])
        self.direction_number = json["DirectionNum"]
        self.latitude = json["Lat"]
        self.longitude = json["Lon"]
        self.route = Route[json["RouteID"]]
        self.trip_end_time = string_to_datetime(json["TripEndTime"])
        self.trip_id = json["TripID"]
        self.trip_start_time = string_to_datetime(json["TripStartTime"])
        self.vehicle_id = json["VehicleID"]


class BusPositions(Response):
    bus_positions: List[BusPosition]

    def __init__(self, json: Dict[str, Any]):
        self.bus_positions = list(
            map(
                BusPosition,
                json["BusPositions"]
            )
        )

class Incident(Response):
    date_updated: datetime
    description: str
    incident_id: str
    incident_type: str
    routes_affected: List[Route]

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.date_updated = string_to_datetime(json["DateUpdated"])
        self.incident_id = json["IncidentID"]
        self.routes_affected = [Route[route] for route in json["RoutesAffected"]]


class Incidents(Response):
    incidents: List[Incident]

    def __init__(self, json: Dict[str, Any]):
        self.incidents = list(
            map(
                Incident,
                json["BusIncidents"]
            )
        )

class PathStop(Response):
    latitude: float
    longitude: float
    sequence_number: int

    def __init__(self, json: Dict[str, Any]):
        self.latitude = json["Lat"]
        self.longitude = json["Lon"]
        self.sequence_number = json["SeqNum"]
        
class PathDirection(Response):
    trip_headsign: str
    direction_text: str
    direction_number: str
    shape: List[PathStop]
    stops: List[Stop]

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.direction_number = json["DirectionNum"]
        self.shape = [PathStop(stop) for stop in json["Shape"]]
        self.stops = [Stop(stop) for stop in json["Stops"]]

class PathDetails(Response):
    route: Route
    name: str
    direction_zero: Optional[PathDirection] = None
    direction_one: Optional[PathDirection] = None

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.route = Route[json["RouteID"]]

        if direction := json["Direction0"]:
            self.direction_zero = PathDirection(direction)

        if direction := json["Direction1"]:
            self.direction_one = PathDirection(direction)

class StopInfo(Response):
    stop: Stop
    stop_name: str
    stop_sequence: int
    time: datetime

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.stop = Stop(json["StopID"])
        self.stop_sequence = json["StopSeq"]
        self.time = string_to_datetime(json["Time"])

class RouteInfo(Response):
    route: Route
    direction_number: str
    trip_direction_text: str
    trip_headsign: str
    start_time: datetime
    end_time: datetime
    stop_times: List[StopInfo]
    trip_id: str

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.route = Route[json["RouteID"]]
        self.direction_number = json["DirectionNum"]
        self.start_time = string_to_datetime(json["StartTime"])
        self.end_time = string_to_datetime(json["EndTime"])
        self.stop_times = [StopInfo(stop_info) for stop_info in json["StopTimes"]]


class RouteSchedule(Response):
    name: str
    direction_zero: List[RouteInfo]
    direction_one: List[RouteInfo]

    def __init__(self, json: Dict[str, Any]):
        self.name = json["Name"]
        self.direction_zero = [RouteInfo(route_info) for route_info in json["Direction0"]]
        self.direction_one = [RouteInfo(route_info) for route_info in json["Direction1"]]


class Prediction(Response):
    direction_number: str
    direction_text: str
    minutes: int
    route: Route
    trip_id: str
    vehicle_id: str

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.direction_number = json["DirectionNum"]
        self.route = Route[json["RouteID"]]
        self.trip_id = json["TripID"]
        self.vehicle_id = json["VehicleID"]

class Predictions(Response):
    predictions: List[Prediction]
    stop_name: str

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.predictions = list(
            map(
                Prediction,
                json["Predictions"]
            )
        )

class Arrival(Response):
    schedule_time: datetime
    direction_number: str
    start_time: datetime
    end_time: datetime
    route: Route
    trip_direction_text: str
    trip_headsign: str
    trip_id: str

    def __init__(self, json: Dict[str, Any]):
        self.schedule_time = string_to_datetime(json["ScheduleTime"])
        self.direction_number = json["DirectionNum"]
        self.start_time = string_to_datetime(json["StartTime"])
        self.end_time = string_to_datetime(json["EndTime"])
        self.route = Route[json["RouteID"]]
        self.trip_id = json["TripID"]

class StopRoutes(Response):
    stop: Stop
    name: str
    latitude: float
    longitude: float
    routes: [Route]

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.stop = Stop(json["StopID"])
        self.latitude = json["Lat"]
        self.longitude = json["Lon"]
        self.routes = [Route[route] for route in json["Routes"]]

class StopSchedule(Response):
    arrivals: List[Arrival]
    stop: StopRoutes

    def __init__(self, json: Dict[str, Any]):
        self.arrivals = [Arrival(arrival) for arrival in json["ScheduleArrivals"]]
        self.stop = StopRoutes(json["Stop"])