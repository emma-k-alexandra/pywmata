from unittest import TestCase
import vcr

from wmata.rail import mixins 
from wmata.rail import responses

class TestRequiresLine(TestCase):
    @vcr.use_cassette('wmata/rail/tests/fixtures/requires_line.yaml')
    def test_stations_on(self):
        requires_line = mixins.RequiresLine()

        response = requires_line.stations_on(
            line=None, 
            api_key="9e38c3eab34c4e6c990828002828f5ed"
        )

        self.assertTrue(isinstance(response, responses.Stations), response)