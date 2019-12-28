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

        self.latitude = json["Lat"]
        self.longitude = json["Lon"]

        self.first_line = Line[json["LineCode1"]]

        self.second_line = get_optional_line(json.get("LineCode2"))
        self.third_line = get_optional_line(json.get("LineCode3"))
        self.fourth_line = get_optional_line(json.get("LineCode4"))

        self.first_station_together = get_optional_station(json.get("StationTogether1"))
        self.second_station_together = get_optional_station(json.get("StationTogether2"))


class Stations(Response):
    stations: List[StationResponse]

    def __init__(self, json: Dict[str, Any]):
        self.stations = list(
            map(
                StationResponse,
                json["Stations"]
            )
        )


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
        self.station_to_station_infos = list(
            map(
                StationToStationInfo, 
                json["StationToStationInfos"]
            )
        )

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
        self.incidents = list(
            map(
                ElevatorAndEscalatorIncident, 
                json["ElevatorIncidents"]
            )
        )

class RailIncident(Response):
    incident_id: str
    description: str
    start_location_full_name: Optional[str]
    end_location_full_name: Optional[str]
    passenger_delay: float
    delay_serverity: Optional[str]
    incident_type: str
    emergency_text: Optional[str]
    lines_affected: str
    date_updated: datetime

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.incident_id = json["IncidentID"]
        self.date_updated = string_to_datetime(json["DateUpdated"])

class RailIncidents(Response):
    incidents: List[RailIncident]

    def __init__(self, json: Dict[str, Any]):
        self.incidents = list(map(RailIncident, json["Incidents"]))

class RailPrediction(Response):
    car: Optional[str]
    destination: str
    destination_station: Optional[Station]
    destination_name: str
    group: str
    line: str
    location: Station
    location_name: str
    minutes: str

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.destination_station = get_optional_station(json["DestinationCode"])
        self.location = Station[json["LocationCode"]]
        self.minutes = json["Min"]

class RailPredictions(Response):
    trains: List[RailPrediction]

    def __init__(self, json: Dict[str, Any]):
        self.trains = list(map(RailPrediction, json["Trains"]))

class StationInformation(Response):
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
        self.latitude = json["Lat"]
        self.longitude = json["Lon"]
        self.first_line = Line[json["LineCode1"]]
        self.second_line = get_optional_line(json["LineCode2"])
        self.third_line = get_optional_line(json["LineCode3"])
        self.fourth_line = get_optional_line(json["LineCode4"])
        self.first_station_together = get_optional_station(json["StationTogether1"])
        self.second_station_together = get_optional_station(json["StationTogether2"])

class ShortTermParking(Response):
    total_count: int
    notes: str

class AllDayParking(Response):
    total_count: int
    rider_cost: Optional[float]
    non_rider_cost: Optional[float]
    saturday_rider_cost: Optional[float]
    saturday_non_rider_cost: Optional[float]

class StationParking(Response):
    station: Station
    notes: Optional[str]
    all_day_parking: AllDayParking
    short_term_parking: ShortTermParking

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.station = Station[json["Code"]]
        self.all_day_parking = AllDayParking(json["AllDayParking"])
        self.short_term_parking = ShortTermParking(json["ShortTermParking"])

class StationsParking(Response):
    stations_parking: List[StationParking]

    def __init__(self, json: Dict[str, Any]):
        self.stations_parking = list(map(StationParking, json["StationsParking"]))

class Path(Response):
    distance_to_previous_station: int
    line: Line
    sequence_number: int
    station: Station
    station_name: str

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.distance_to_previous_station = json["DistanceToPrev"]
        self.line = Line[json["LineCode"]]
        self.sequence_number = json["SeqNum"]
        self.station = Station[json["StationCode"]]

class PathBetweenStations(Response):
    path: List[Path]

    def __init__(self, json: Dict[str, Any]):
        self.path = list(map(Path, json["Path"]))

class TrainTime(Response):
    time: str
    destination: Station

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.destination = Station[json["DestinationStation"]]

class StationFirstLastTrains(Response):
    opening_time: str
    first_trains: List[TrainTime]
    last_trains: List[TrainTime]

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.first_trains = list(map(TrainTime, json["FirstTrains"]))
        self.last_trains = list(map(TrainTime, json["LastTrains"]))

class StationTime(Response):
    station: Station
    station_name: str
    # You're gonna love this
    monday: StationFirstLastTrains
    tuesday: StationFirstLastTrains
    wednesday: StationFirstLastTrains
    thursday: StationFirstLastTrains
    friday: StationFirstLastTrains
    saturday: StationFirstLastTrains
    sunday: StationFirstLastTrains

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.station = Station[json["Code"]]
        self.monday = StationFirstLastTrains(json["Monday"])
        self.tuesday = StationFirstLastTrains(json["Tuesday"])
        self.wednesday = StationFirstLastTrains(json["Wednesday"])
        self.thursday = StationFirstLastTrains(json["Thursday"])
        self.friday = StationFirstLastTrains(json["Friday"])
        self.saturday = StationFirstLastTrains(json["Saturday"])
        self.sunday = StationFirstLastTrains(json["Sunday"])

class StationTimings(Response):
    station_times: List[StationTime]

    def __init__(self, json: Dict[str, Any]):
        self.station_times = list(map(StationTime, json["StationTimes"]))

class LineResponse(Response):
    line: Line
    display_name: str
    start_station: Station
    end_station: Station
    first_internal_destination: Optional[Station]
    second_internal_destination: Optional[Station]

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.line = Line[json["LineCode"]]
        self.start_station = Station[json["StartStationCode"]]
        self.end_station = Station[json["EndStationCode"]]
        self.first_internal_destination = get_optional_station(json["InternalDestination1"])
        self.second_internal_destination = get_optional_station(json["InternalDestination2"])

class Lines(Response):
    lines: List[LineResponse]

    def __init__(self, json: Dict[str, Any]):
        self.lines = list(map(LineResponse, json["Lines"]))

class StationEntrance(Response):
    description: str
    identifier: str
    latitude: float
    longitude: float
    name: str
    first_station: Station
    second_station: Optional[Station]

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.identifier = json["ID"]
        self.latitude = json["Lat"]
        self.longitude = json["Lon"]
        self.first_station = Station[json["StationCode1"]]
        self.second_station = get_optional_station(json["StationCode2"])

class StationEntrances(Response):
    entrances: List[StationEntrance]

    def __init__(self, json: Dict[str, Any]):
        self.entrances = list(map(StationEntrance, json["Entrances"]))

class TrainPosition(Response):
    train_id: str
    train_number: str
    car_count: int
    direction_number: int
    circuit_id: int
    destination_station: Optional[Station]
    line: Optional[Line]
    seconds_at_location: int
    service_type: str

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.direction_number = json["DirectionNum"]

        self.destination_station = get_optional_station(json["DestinationStationCode"])
        self.line = get_optional_line(json["LineCode"])

class TrainPositions(Response):
    train_positions: List[TrainPosition]

    def __init__(self, json: Dict[str, Any]):
        self.train_positions = list(map(TrainPosition, json["TrainPositions"]))

class TrackCircuitWithStation(Response):
    sequence_number: int
    circuit_id: int
    station: Optional[Station]

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.sequence_number = json["SeqNum"]
        self.station = get_optional_station(json["StationCode"])

class StandardRoute(Response):
    line: Line
    track_number: int
    track_circuits: List[TrackCircuitWithStation]

    def __init__(self, json: Dict[str, Any]):
        self.line = Line[json["LineCode"]]
        self.track_number = json["TrackNum"]
        self.track_circuits = list(map(TrackCircuitWithStation, json["TrackCircuits"]))

class StandardRoutes(Response):
    standard_routes: List[StandardRoute]

    def __init__(self, json: Dict[str, Any]):
        self.standard_routes = list(map(StandardRoute, json["StandardRoutes"]))

class TrackNeighbor(Response):
    neighbor_type: str
    circuit_ids: List[int]

class TrackCircuit(Response):
    track: int
    circuit_id: int
    neighbors: List[TrackNeighbor]

    def __init__(self, json: Dict[str, Any]):
        super().__init__(json)

        self.neighbors = list(map(TrackNeighbor, json["Neighbors"]))

class TrackCircuits(Response):
    track_circuits: List[TrackCircuit]

    def __init__(self, json: Dict[str, Any]):
        self.track_circuits = list(map(TrackCircuit, json["TrackCircuits"]))
