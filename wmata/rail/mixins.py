from typing import Optional, Union
from .urls import URLs
from . import responses
from .line import Line
from .station import Station
from ..mixins import Fetcher
from ..error import WMATAError

class RequiresLine(Fetcher):
    """Methods that require a Line
    """
    def stations_on(self, line: Optional[Line], api_key: str) -> Union[responses.Stations, WMATAError]:
        """Stations on the given line
        
        Arguments:
            line {Optional[Line]} -- Optional Line to get stations along
            api_key {str} -- API Key to make this request with
        
        Returns:
            Union[responses.Stations, WMATAError] -- Response from WMATA API, either {}
        """
        params = {}

        if line:
            params["line"] = line.name

        return self.fetch(
            URLs.Stations.value,
            params=params,
            api_key=api_key,
            output_class=responses.Stations
        )

class RequiresStation(Fetcher):
    """Methods that require a Station
    """
    def station_to_station(self, from_station: Optional[Station], destination_station: Optional[Station], api_key: str) -> Union[responses.StationToStationInfos, WMATAError]:
        """ Distance, fare information, and estimated travel time between any two stations, including those on different lines.
        WMATA Documentation: https://developer.wmata.com/docs/services/5476364f031f590f38092507/operations/5476364f031f5909e4fe3313?
        
        Arguments:
            from_station {Optional[Station]} -- Station to start from
            destination_station {Optional[Station]} -- Ending station
            api_key {str} -- WMATA API key
        
        Returns:
            Union[StationToStationInfos, WMATAError]
        """
        params = {}

        if from_station:
            params["FromStationCode"] = from_station.value

        if destination_station:
            params["ToStationCode"] = destination_station.value

        return self.fetch(
            URLs.StationToStation.value,
            params=params,
            api_key=api_key,
            output_class=responses.StationToStationInfos
        )

    def elevator_and_escalator_incidents_at(self, station: Optional[Station], api_key: str) -> Union[responses.ElevatorAndEscalatorIncidents, WMATAError]:
        """List of reported elevator and escalator outages at a given station.
        WMATA Documentation https://developer.wmata.com/docs/services/54763641281d83086473f232/operations/54763641281d830c946a3d76?
        
        Arguments:
            station {Optional[Station]} -- Station to check for incidents at
            api_key {str} -- WMATA API Key
        
        Returns:
            Union[responses.ElevatorAndEscalatorIncidents, WMATAError]
        """
        params = {}

        if station:
            params["StationCode"] = station.value

        return self.fetch(
            URLs.ElevatorAndEscalatorIncidents.value,
            params=params,
            api_key=api_key,
            output_class=responses.ElevatorAndEscalatorIncidents
        )
        
    def incidents_at(self, station: Optional[Station], api_key: str) -> Union[responses.RailIncidents, WMATAError]:
        """Reported rail incidents (significant disruptions and delays to normal service)
        WMATA Documentation https://developer.wmata.com/docs/services/54763641281d83086473f232/operations/54763641281d830c946a3d77?
        
        Arguments:
            station {Optional[Station]} -- Station to check for incidents api
            api_key {str} -- WMATA API Key
        
        Returns:
            Union[RailIncidents, WMATAError]
        """
        params = {}

        if station:
            params["StationCode"] = station.value

        return self.fetch(
            URLs.Incidents.value,
            params=params,
            api_key=api_key,
            output_class=responses.RailIncidents
        )
