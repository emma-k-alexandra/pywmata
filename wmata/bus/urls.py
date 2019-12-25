"""URLs for all MetroBus endpoints
"""
from enum import Enum

class URLs(Enum):
    """URLs for all MetroBus endpoints
    """
    Routes = "https://api.wmata.com/Bus.svc/json/jRoutes"
    Stops = "https://api.wmata.com/Bus.svc/json/jStops"
    Incidents = "https://api.wmata.com/Incidents.svc/json/BusIncidents"
    Positions = "https://api.wmata.com/Bus.svc/json/jBusPositions"
    PathDetails = "https://api.wmata.com/Bus.svc/json/jRouteDetails"
    RouteSchedule = "https://api.wmata.com/Bus.svc/json/jRouteSchedule"
    NextBuses = "https://api.wmata.com/NextBusService.svc/json/jPredictions"
    StopSchedule = "https://api.wmata.com/Bus.svc/json/jStopSchedule"