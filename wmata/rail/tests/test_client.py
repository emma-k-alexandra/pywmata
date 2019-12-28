from unittest import TestCase
import vcr

from .utils import VCR_STORAGE
from ..client import MetroRail
from .. import responses
from ...tests.utils import API_KEY
from ...location import RadiusAtCoordinates, Coordinates

class TestMetroRail(TestCase):
    def setUp(self):
        self.metro_rail = MetroRail(API_KEY)

    @vcr.use_cassette(VCR_STORAGE.format('lines'))
    def test_lines(self):
        response = self.metro_rail.lines()
        self.assertIsInstance(response, responses.Lines)

    @vcr.use_cassette(VCR_STORAGE.format('entrances'))
    def test_entrances(self):
        response = self.metro_rail.entrances(RadiusAtCoordinates(1, Coordinates(1.0, 1.0)))

        self.assertIsInstance(response, responses.StationEntrances)

    @vcr.use_cassette(VCR_STORAGE.format('positions'))
    def test_positions(self):
        response = self.metro_rail.positions()

        self.assertIsInstance(response, responses.TrainPositions)

    @vcr.use_cassette(VCR_STORAGE.format('routes'))
    def test_routes(self):
        response = self.metro_rail.routes()

        self.assertIsInstance(response, responses.StandardRoutes)

    @vcr.use_cassette(VCR_STORAGE.format('circuits'))
    def test_circuits(self):
        response = self.metro_rail.circuits()

        self.assertIsInstance(response, responses.TrackCircuits)
