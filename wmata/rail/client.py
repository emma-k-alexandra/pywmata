"""For interacting with MetroRail endpoints
"""
import functools
from typing import Optional, Callable, Union
from . import mixins, responses, line, station
from ..error import WMATAError

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
            self.timings,
            api_key=self.key
        )
