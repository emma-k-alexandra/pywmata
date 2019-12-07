"""Successful responses from the WMATA API
"""
from typing import List, Optional, Dict, Any
from datetime import datetime
from .station import Station
from .line import Line
from ..utils import to_snake_case
from ..responses import Response
from ..date import string_to_datetime

def get_optional_line(value: Any) -> Optional[Line]:
    try:
        return Line[value]

    except KeyError:
        return None

def get_optional_station(value: Any) -> Optional[Station]:
    try:
        return Station[value]

    except KeyError:
        return None

class Address(Response):
    city: str
    state: str
    street: str
    zipcode: str


class StationResponse(Response):
    address: Address
    station: Station
    latitude: float
    longitude: float
    first_line: Line
    second_line: Optional[Line]
    third_line: Optional[Line]
    fourth_line: Optional[Line]
    name: str
    first_station_together: Optional[Station]
    second_station_together: Optional[Station]

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.address = Address(json["Address"])
        self.station = Station[json["Code"]]

        self.first_line = Line[json["LineCode1"]]

        self.second_line = get_optional_line(json.get("LineCode2"))
        self.third_line = get_optional_line(json.get("LineCode3"))
        self.fourth_line = get_optional_line(json.get("LineCode4"))

        self.first_station_together = get_optional_station(json.get("StationTogether1"))
        self.second_station_together = get_optional_station(json.get("StationTogether2"))


class Stations(Response):
    stations: List[StationResponse]

    def __init__(self, json: Dict[str, Any]):
        self.stations = [StationResponse(station_json) for station_json in json["Stations"]]


class RailFare(Response):
    off_peak_time: float
    peak_time: float
    senior_disabled: float


class StationToStationInfo(Response):
    composite_miles: str
    destination: Station
    rail_fare: RailFare
    rail_time: int
    source: Station

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.destination = Station[json["DestinationStation"]]
        self.rail_fare = RailFare(json["RailFare"])
        self.source = Station[json["SourceStation"]]

class StationToStationInfos(Response):
    station_to_station_infos: List[StationToStationInfo]

    def __init__(self, json: Dict[str, Any]):
        self.station_to_station_infos = [
            StationToStationInfo(station_to_station_info_json) 
            for station_to_station_info_json 
            in json["StationToStationInfos"]
        ]

class ElevatorAndEscalatorIncident(Response):
    unit_name: str
    unit_type: str
    unit_status: Optional[str]
    station: Station
    station_name: str
    location_description: str
    symptom_code: str
    time_out_of_service: str
    symptom_description: str
    display_order: float
    date_out_of_service: datetime
    date_updated: datetime
    estimated_return_to_service: Optional[datetime]

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.station = Station[json["StationCode"]]
        self.date_out_of_service = string_to_datetime(json["DateOutOfServ"])
        self.date_updated = string_to_datetime(json["DateUpdated"])
        
        # TODO: This could probably be written a little fancier
        if estimated_return_to_service := json["EstimatedReturnToService"]:
            self.estimated_return_to_service = string_to_datetime(estimated_return_to_service)

        else:
            self.estimated_return_to_service = None


class ElevatorAndEscalatorIncidents(Response):
    incidents: List[ElevatorAndEscalatorIncident]

    def __init__(self, json: Dict[str, Any]):
        self.incidents = [
            ElevatorAndEscalatorIncident(elevator_and_escalator_incident_json)
            for elevator_and_escalator_incident_json
            in json["ElevatorIncidents"]
        ]
