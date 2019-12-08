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
    def _stations_on(self, line: Optional[Line], api_key: str) -> Union[responses.Stations, WMATAError]:
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
    def _station_to_station(self, from_station: Optional[Station], destination_station: Optional[Station], api_key: str) -> Union[responses.StationToStationInfos, WMATAError]:
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

    def _elevator_and_escalator_incidents_at(self, station: Optional[Station], api_key: str) -> Union[responses.ElevatorAndEscalatorIncidents, WMATAError]:
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
        
    def _incidents_at(self, station: Optional[Station], api_key: str) -> Union[responses.RailIncidents, WMATAError]:
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

    def _next_trains(self, station: Station, api_key: str) -> Union[responses.RailPredictions, WMATAError]:
        """Next train arrivals for the given station.
        WMATA Documentation https://developer.wmata.com/docs/services/547636a6f9182302184cda78/operations/547636a6f918230da855363f
        
        Arguments:
            station {Station} -- Station to get next trains at
            api_key {str} -- WMATA API Key
        
        Returns:
            Union[responses.RailPredictions, WMATAError]
        """
        return self.fetch(
            '/'.join([URLs.NextTrains.value, station.value]),
            params={},
            api_key=api_key,
            output_class=responses.RailPredictions
        )

    def _station_information(self, station: Station, api_key: str) -> Union[responses.StationInformation, WMATAError]:
        """Location and address information at the given station.
        WMATA Documentation https://developer.wmata.com/docs/services/5476364f031f590f38092507/operations/5476364f031f5909e4fe3310?
        
        Arguments:
            station {Station} -- Station to get information for
            api_key {str} -- WMATA API Key
        
        Returns:
            Union[responses.StationInformation, WMATAError]
        """
        return self.fetch(
            URLs.Information.value,
            params={"StationCode": station.value},
            api_key=api_key,
            output_class=responses.StationInformation
        )

    def _parking_information(self, station: Station, api_key: str) -> Union[responses.StationsParking, WMATAError]:
        """Parking information for the given station.
        
        Arguments:
            station {Station} -- Station to get parking information for
            api_key {str} -- WMATA API Key
        
        Returns:
            Union[responses.StationsParking, WMATAError]
        """
        return self.fetch(
            URLs.ParkingInformation.value,
            params={"StationCode": station.value},
            api_key=api_key,
            output_class=responses.StationsParking
        )

    def _path_from(self, station: Station, destination_station: Station, api_key: str) -> Union[responses.PathBetweenStations, WMATAError]:
        """Set of ordered stations and distances between two stations on the **same line**.
        
        Arguments:
            station {Station} -- Starting station
            destination_station {Station} -- Ending station
            api_key {str} -- WMATA API Key
        
        Returns:
            Union[responses.PathBetweenStations, WMATAError]
        """
        return self.fetch(
            URLs.Path.value,
            params={
                "FromStationCode": station.value,
                "ToStationCode": destination_station.value
            },
            api_key=api_key,
            output_class=responses.PathBetweenStations
        )

    def _timings(self, station: Station, api_key: str) -> Union[responses.StationTimings, WMATAError]:
        """Opening and scheduled first/last train times for the given station.
        
        Arguments:
            station {Station} -- Station to get schedule for
            api_key {str} -- WMATA API Key
        
        Returns:
            Union[responses.StationTimings, WMATAError]
        """
        return self.fetch(
            URLs.Timings.value,
            params={"StationCode": station.value},
            api_key=api_key,
            output_class=responses.StationTimings
        )
