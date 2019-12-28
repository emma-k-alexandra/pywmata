"""For interacting with MetroBus endpoints
"""
import functools
from typing import Optional, Callable, Union
from . import mixins, route, stop, urls, responses
from ..date import Date
from ..error import WMATAError
from ..location import RadiusAtCoordinates

class MetroBus(mixins.RequiresRoute, mixins.RequiresStop):
    key: str

    #RequiresRoute
    positions_along: Callable[[Optional[route.Route], Optional[RadiusAtCoordinates]], Union[responses.BusPositions, WMATAError]]
    incidents_along: Callable[[Optional[route.Route]], Union[responses.Incidents, WMATAError]]
    path: Callable[[route.Route, Optional[Date]], Union[responses.PathDetails, WMATAError]]
    route_schedule: Callable[[route.Route, Optional[Date], bool], Union[responses.RouteSchedule, WMATAError]]

    #RequiresStop
    next_buses: Callable[[stop.Stop], Union[responses.Predictions, WMATAError]]
    stop_schedule: Callable[[stop.Stop, Optional[Date]], Union[responses.StopSchedule, WMATAError]]

    def __init__(self, key: str):
        self.key = key

        #RequiresRoute
        self.positions_along = functools.partial(
            self._positions_along, 
            api_key=self.key
        )

        self.incidents_along = functools.partial(
            self._incidents_along,
            api_key=self.key
        )

        self.path = functools.partial(
            self._path,
            api_key=self.key
        )

        self.route_schedule = functools.partial(
            self._route_schedule,
            api_key=self.key
        )

        #RequiresStop
        self.next_buses = functools.partial(
            self._next_buses,
            api_key=self.key
        )

        self.stop_schedule = functools.partial(
            self._stop_schedule,
            api_key=self.key
        )

    def routes(self) -> Union[responses.Routes, WMATAError]:
        return self.fetch(
            urls.URLs.Routes.value,
            params={},
            api_key=self.key,
            output_class=responses.Routes
        )

    def stops(self, radius_at_coordinates: Optional[RadiusAtCoordinates]) -> Union[responses.Stops, WMATAError]:
        params = {}

        if radius_at_coordinates:
            params = radius_at_coordinates.to_dict()

        return self.fetch(
            urls.URLs.Stops.value,
            params= params,
            api_key=self.key,
            output_class=responses.Stops
        )
