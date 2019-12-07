"""Successful responses from the WMATA API
"""
from typing import List, Optional, Dict, Any
from .station import Station
from .line import Line
from ..utils import to_snake_case

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

class Address:
    city: str
    state: str
    street: str
    zipcode: str

    def __init__(self, json: Dict[str, Any]):
        for key, value in json.items():
            setattr(self, to_snake_case(key), value)


class StationResponse:
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
        for key, value in json.items():
            setattr(self, to_snake_case(key), value)

        self.address = Address(json["Address"])
        self.station = Station[json["Code"]]

        self.first_line = Line[json["LineCode1"]]

        self.second_line = get_optional_line(json.get("LineCode2"))
        self.third_line = get_optional_line(json.get("LineCode3"))
        self.fourth_line = get_optional_line(json.get("LineCode4"))

        self.first_station_together = get_optional_station(json.get("StationTogether1"))
        self.second_station_together = get_optional_station(json.get("StationTogether2"))


class Stations:
    stations: List[StationResponse]

    def __init__(self, json: Dict[str, Any]):
        self.stations = [StationResponse(station_json) for station_json in json["Stations"]]


class StationToStationInfo:
    composite_miles: str
    destination: Station
    rail_fare: RailFare
    rail_time: int
    source: Station

    def __init__(self, json: Dict[str, Any]):
        for key, value in json.items():
            setattr(self, to_snake_case(key), value)

        self.destination = Station[json["DestinationStation"]]
        self.rail_fare = RailFare(json["RailFare"])
        self.source = Station[json["SourceStation"]]
        
class StationToStationInfos:
    station_to_station_infos: List[StationToStationInfo]

    def __init__(self, json: Dict[str, Any]):
        self.station_to_station_infos = [
            StationToStationInfo(station_to_station_info_json) 
            for station_to_station_info_json 
            in json["StationToStationInfos"]
        ]


class 
