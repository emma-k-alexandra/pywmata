from unittest import TestCase
import vcr

from wmata.bus import mixins, responses, route, stop
from wmata.location import RadiusAtCoordinates, Coordinates
from wmata.date import Date
from .utils import VCR_STORAGE
from ...tests.utils import API_KEY

class TestRequiresRoute(TestCase):
    def setUp(self):
        self.requires_route = mixins.RequiresRoute()

    @vcr.use_cassette(VCR_STORAGE.format('positions_along'))
    def test_positions_along(self):
        response = self.requires_route._positions_along(
            route=None,
            radius_at_coordinates=None,
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.BusPositions)
    
    @vcr.use_cassette(VCR_STORAGE.format('positions_along_route'))
    def test_positions_along_route(self):
        response = self.requires_route._positions_along(
            route=route.Route["_10A"],
            radius_at_coordinates=None,
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.BusPositions)

    @vcr.use_cassette(VCR_STORAGE.format('positions_along_route_at'))
    def test_positions_along_route_at(self):
        response = self.requires_route._positions_along(
            route=route.Route["_10A"],
            radius_at_coordinates=RadiusAtCoordinates(
                500,
                Coordinates(
                    38.8817596,
                    -77.0166426
                )
            ),
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.BusPositions)

    @vcr.use_cassette(VCR_STORAGE.format('incidents_along'))
    def test_incidents_along(self):
        response = self.requires_route._incidents_along(
            route=None,
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.Incidents)

    @vcr.use_cassette(VCR_STORAGE.format('incidents_along_route'))
    def test_incidents_along_route(self):
        response = self.requires_route._incidents_along(
            route=route.Route["_10A"],
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.Incidents)
    
    @vcr.use_cassette(VCR_STORAGE.format('path'))
    def test_path(self):
        response = self.requires_route._path(
            route=route.Route["_10A"],
            date=None,
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.PathDetails)

    @vcr.use_cassette(VCR_STORAGE.format('path_with_date'))
    def test_path_with_date(self):
        response = self.requires_route._path(
            route=route.Route["_10A"],
            date=Date(2019, 12, 28),
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.PathDetails)

    @vcr.use_cassette(VCR_STORAGE.format('route_schedule'))
    def test_route_schedule(self):
        response = self.requires_route._route_schedule(
            route=route.Route["_10A"],
            date=None,
            including_variations=False,
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.RouteSchedule)

    @vcr.use_cassette(VCR_STORAGE.format('route_schedule_with_date'))
    def test_route_schedule_with_date(self):
        response = self.requires_route._route_schedule(
            route=route.Route["_10A"],
            date=Date(2019, 12, 28),
            including_variations=False,
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.RouteSchedule)

    @vcr.use_cassette(VCR_STORAGE.format('route_schedule_with_date_including_variations'))
    def test_route_schedule_with_date_including_variations(self):
        response = self.requires_route._route_schedule(
            route=route.Route["_10A"],
            date=Date(2019, 12, 28),
            including_variations=True,
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.RouteSchedule)

class TestRequiresStop(TestCase):
    def setUp(self):
        self.requires_stop = mixins.RequiresStop()

    @vcr.use_cassette(VCR_STORAGE.format('next_buses'))
    def test_next_buses(self):
        response = self.requires_stop._next_buses(
            stop=stop.Stop(identifier="3003037"),
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.Predictions)

    @vcr.use_cassette(VCR_STORAGE.format('stop_schedule'))
    def test_stop_schedule(self):
        response = self.requires_stop._stop_schedule(
            stop=stop.Stop(identifier="3003037"),
            date=None,
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.StopSchedule)

    @vcr.use_cassette(VCR_STORAGE.format('stop_schedule_with_date'))
    def test_stop_schedule_with_date(self):
        response = self.requires_stop._stop_schedule(
            stop=stop.Stop(identifier="3003037"),
            date=Date(2019, 12, 28),
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.StopSchedule)