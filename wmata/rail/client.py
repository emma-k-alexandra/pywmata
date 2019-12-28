"""For interacting with MetroRail endpoints
"""
import functools
from typing import Optional, Callable, Union
from . import mixins, responses, line, station, urls
from ..error import WMATAError
from ..location import RadiusAtCoordinates

class MetroRail(mixins.RequiresLine, mixins.RequiresStation):
    """Main object for interacting with MetroRail API methods
    """
    key: str

    #RequiresLine
    stations_on: Callable[[Optional[line.Line]], Union[responses.Stations, WMATAError]]

    #RequiresStation
    station_to_station: Callable[[Optional[station.Station], Optional[station.Station]], Union[responses.StationToStationInfos, WMATAError]]
    elevator_and_escalator_incidents_at: Callable[[Optional[station.Station]], Union[responses.ElevatorAndEscalatorIncidents, WMATAError]]
    incidents_at: Callable[[Optional[station.Station]], Union[responses.RailIncidents, WMATAError]]
    next_trains: Callable[[station.Station], Union[responses.RailPredictions, WMATAError]]
    station_information: Callable[[station.Station], Union[responses.StationInformation, WMATAError]]
    parking_information: Callable[[station.Station], Union[responses.StationsParking, WMATAError]]
    path_from: Callable[[station.Station, station.Station], Union[responses.PathBetweenStations, WMATAError]]
    timings: Callable[[station.Station], Union[responses.StationTimings, WMATAError]]

    def __init__(self, key: str):
        self.key = key

        # RequiresLine
        self.stations_on = functools.partial(self._stations_on, api_key=self.key)
        
        #RequiresStation
        self.station_to_station = functools.partial(
            self._station_to_station, 
            api_key=self.key
        )

        self.elevator_and_escalator_incidents_at = functools.partial(
            self._elevator_and_escalator_incidents_at, 
            api_key=self.key
        )

        self.incidents_at = functools.partial(
            self._incidents_at,
            api_key=self.key
        )

        self.next_trains = functools.partial(
            self._next_trains,
            api_key=self.key
        )

        self.station_information = functools.partial(
            self._station_information,
            api_key=self.key
        )

        self.parking_information = functools.partial(
            self._parking_information,
            api_key=self.key
        )

        self.path_from = functools.partial(
            self._path_from,
            api_key=self.key
        )

        self.timings = functools.partial(
            self._timings,
            api_key=self.key
        )

    def lines(self) -> Union[responses.Lines, WMATAError]:
        """Basic information on all MetroRail lines.
        WMATA Documentation https://developer.wmata.com/docs/services/5476364f031f590f38092507/operations/5476364f031f5909e4fe330c
        
        Returns:
            Union[responses.Lines, WMATAError]
        """
        return self.fetch(
            urls.URLs.Lines.value,
            params={},
            api_key=self.key,
            output_class=responses.Lines
        )

    def entrances(self, radiusAtCoordinates: RadiusAtCoordinates) -> Union[responses.StationEntrances, WMATAError]:
        """Nearby station entrances based on latitude, longitude, and radius (meters).
        WMATA Documentation https://developer.wmata.com/docs/services/5476364f031f590f38092507/operations/5476364f031f5909e4fe330f?

        Arguments:
            radiusAtCoordinates {RadiusAtCoordinates} -- Area to search for entrances within
        
        Returns:
            Union[responses.StationEntrances, WMATAError]
        """
        return self.fetch(
            urls.URLs.Entrances.value,
            params=radiusAtCoordinates.to_dict(),
            api_key=self.key,
            output_class=responses.StationEntrances
        )

    def positions(self) -> Union[responses.TrainPositions, WMATAError]:
        """Uniquely identifiable trains in service and what track circuits they currently occupy.
        WMATA Documentation https://developer.wmata.com/docs/services/5763fa6ff91823096cac1057/operations/5763fb35f91823096cac1058
        
        Returns:
            Union[responses.TrainPositions, WMATAError] -- [description]
        """
        return self.fetch(
            urls.URLs.Positions.value,
            params={"contentType": "json"},
            api_key=self.key,
            output_class=responses.TrainPositions
        )

    def routes(self) -> Union[responses.StandardRoutes, WMATAError]:
        """Returns an ordered list of mostly revenue (and some lead) track circuits, arranged by line and track number.
        WMATA Documentation https://developer.wmata.com/docs/services/5763fa6ff91823096cac1057/operations/57641afc031f59363c586dca?
        
        Returns:
            Union[responses.StandardRoutes, WMATAError]
        """
        return self.fetch(
            urls.URLs.Routes.value,
            params={"contentType": "json"},
            api_key=self.key,
            output_class=responses.StandardRoutes
        )

    def circuits(self) -> Union[responses.TrackCircuits, WMATAError]:
        """All track circuits including those on pocket tracks and crossovers. Each track circuit may include references to its right and left neighbors.
        WMATA Documentation https://developer.wmata.com/docs/services/5763fa6ff91823096cac1057/operations/57644238031f59363c586dcb?
        
        Returns:
            Union[responses.TrackCircuits, WMATAError] -- [description]
        """
        return self.fetch(
            urls.URLs.Circuits.value,
            params={"contentType": "json"},
            api_key=self.key,
            output_class=responses.TrackCircuits
        )
