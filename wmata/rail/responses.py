"""Successful responses from the WMATA API
"""
from typing import List, Optional, Dict, Any
from .station import Station
from .line import Line

class Address:
    city: str
    state: str
    street: str
    zipcode: str


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


class Stations:
    stations: List[StationResponse]

    def __init__(self, json: Dict[str, Any]):
        for key, value in json.items():
            setattr(self, key, value)

        self.address = StationResponse(json["Address"])
        self.station = Station[json["StationCode"]]

        self.first_line = Line[json["LineCode1"]]
        
        try:
            self.second_line = Line[json.get("LineCode2")]
        
        except KeyError:
            self.second_line = None

        if third_line := json.get("LineCode3"):
            self.third_line = third_line

        if fourth_line := json.get("LineCode4"):
            self.fourth_line = fourth_line