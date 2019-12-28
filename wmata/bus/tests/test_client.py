from unittest import TestCase
import vcr

from .utils import VCR_STORAGE
from wmata.bus.client import MetroBus
from .. import responses
from ...tests.utils import API_KEY
from ...location import RadiusAtCoordinates, Coordinates

class TestMetroBus(TestCase):
    def setUp(self):
        self.metro_bus = MetroBus(API_KEY)

    @vcr.use_cassette(VCR_STORAGE.format('routes'))
    def test_routes(self):
        response = self.metro_bus.routes()

        self.assertIsInstance(response, responses.Routes)

    @vcr.use_cassette(VCR_STORAGE.format('stops'))
    def test_stops(self):
        response = self.metro_bus.stops(
            radius_at_coordinates=None
        )

        self.assertIsInstance(response, responses.Stops)

    @vcr.use_cassette(VCR_STORAGE.format('stops_at_coordinates'))
    def test_stops_at_coordinates(self):
        response = self.metro_bus.stops(
            radius_at_coordinates=RadiusAtCoordinates(
                500,
                coordinates=Coordinates(
                    latitude=38.8817596,
                    longitude=-77.0166426
                )
            )
        )

        self.assertIsInstance(response, responses.Stops)
    