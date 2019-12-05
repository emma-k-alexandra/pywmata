"""URLs for all MetroRail endpoints
"""
from enum import Enum

class URLs(Enum):
    """URLs for all MetroRail endpoints
    """
    NextTrains = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction"
    Information = "https://api.wmata.com/Rail.svc/json/jStationInfo"
    ParkingInformation = "https://api.wmata.com/Rail.svc/json/jStationParking"
    Path = "https://api.wmata.com/Rail.svc/json/jPath"
    Timings = "https://api.wmata.com/Rail.svc/json/jStationTimes"
    StationToStation = "https://api.wmata.com/Rail.svc/json/jSrcStationToDstStationInfo"
    Lines = "https://api.wmata.com/Rail.svc/json/jLines"
    Entrances = "https://api.wmata.com/Rail.svc/json/jStationEntrances"
    Positions = "https://api.wmata.com/TrainPositions/TrainPositions"
    Routes = "https://api.wmata.com/TrainPositions/StandardRoutes"
    Circuits = "https://api.wmata.com/TrainPositions/TrackCircuits"
    ElevatorAndEscalatorIncidents = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
    Incidents = "https://api.wmata.com/Incidents.svc/json/Incidents"
    Stations = "https://api.wmata.com/Rail.svc/json/jStations"
