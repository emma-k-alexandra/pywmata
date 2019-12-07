from typing import Optional, Union
from .urls import URLs
from .responses import Stations, StationToStationInfos
from .line import Line
from .station import Station
from ..mixins import Fetcher
from ..error import WMATAError

class RequiresLine(Fetcher):
    """Methods that require a Line
    """
    def stations_on(self, line: Optional[Line], api_key: str) -> Union[Stations, WMATAError]:
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
            output_class=Stations
        )

class RequiresStation(Fetcher):
    """Methods that require a Station
    """
    def station_to_station(self, from_station: Optional[Station], destination_station: Optional[Station], api_key: str) -> Union[StationToStationInfos, WMATAError]:
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
            output_class=StationToStationInfos
        )
        
