from typing import Optional, Union
from . import responses
from .urls import URLs
from .route import Route
from .stop import Stop
from ..mixins import Fetcher
from ..location import RadiusAtCoordinates
from ..error import WMATAError
from ..date import Date

class RequiresRoute(Fetcher):
    """Methods that require a Route
    """
    def _positions_along(self, route: Optional[Route], radius_at_coordinates: Optional[RadiusAtCoordinates], api_key: str) -> Union[responses.BusPositions, WMATAError]:
        params = {}

        if route:
            params["Route"] = route.name

        if radius_at_coordinates:
            params.update(radius_at_coordinates.to_dict())

        return self.fetch(
            URLs.Positions.value,
            params=params,
            api_key=api_key,
            output_class=responses.BusPositions
        )
    

    def _incidents_along(self, route: Optional[Route], api_key: str) -> Union[responses.Incidents, WMATAError]:
        params = {}

        if route:
            params["Route"] = route.value

        return self.fetch(
            URLs.Incidents.value,
            params=params,
            api_key=api_key,
            output_class=responses.Incidents
        )

    def _path(self, route: Route, date: Optional[Date], api_key: str) -> Union[responses.PathDetails, WMATAError]:
        params = {
            "RouteID": route.value
        }

        if date:
            params["Date"] = str(date)

        return self.fetch(
            URLs.PathDetails.value,
            params=params,
            api_key=api_key,
            output_class=responses.PathDetails
        )

    def _route_schedule(self, route: Route, date: Optional[Date], including_variations: bool, api_key: str) -> Union[responses.RouteSchedule, WMATAError]:
        params = {
            "RouteID": route.value
        }

        if date:
            params["Date"] = str(date)

        if including_variations:
            params["IncludingVariations"] = "{}".format(including_variations).lower()

        return self.fetch(
            URLs.RouteSchedule.value,
            params=params,
            api_key=api_key,
            output_class=responses.RouteSchedule
        )

class RequiresStop(Fetcher):
    """Methods that require a Stop
    """
    def _next_buses(self, stop: Stop, api_key: str) -> Union[responses.Predictions, WMATAError]:
        return self.fetch(
            URLs.NextBuses.value,
            params={"StopID": stop.identifier},
            api_key=api_key,
            output_class=responses.Predictions
        )

    def _stop_schedule(self, stop: Stop, date: Optional[Date], api_key) -> Union[responses.StopSchedule, WMATAError]:
        params = {
            "StopID": stop.identifier
        }

        if date:
            params["Date"] = str(date)

        return self.fetch(
            URLs.StopSchedule.value,
            params=params,
            api_key=api_key,
            output_class=responses.StopSchedule
        )
