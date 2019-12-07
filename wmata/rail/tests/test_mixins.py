from unittest import TestCase
import vcr

from wmata.rail import mixins, responses, line, station

API_KEY = "9e38c3eab34c4e6c990828002828f5ed"
VCR_STORAGE = "wmata/rail/tests/fixtures/{}.yaml"

class TestRequiresLine(TestCase):
    def setUp(self):
        self.requires_line = mixins.RequiresLine()

    @vcr.use_cassette(VCR_STORAGE.format('stations_on'))
    def test_stations_on(self):
        response = self.requires_line.stations_on(
            line=None, 
            api_key=API_KEY
        )

        self.assertTrue(isinstance(response, responses.Stations), response)

    @vcr.use_cassette(VCR_STORAGE.format('stations_on_blue_line'))
    def test_stations_on_blue_line(self):
        response = self.requires_line.stations_on(
            line=line.Line["BL"],
            api_key=API_KEY
        )

        self.assertTrue(isinstance(response, responses.Stations), response)


class TestRequiresStation(TestCase):
    def setUp(self):
        self.requires_station = mixins.RequiresStation()

    @vcr.use_cassette(VCR_STORAGE.format('station_to_station_infos'))
    def test_station_to_station(self):
        response = self.requires_station.station_to_station(
            from_station=None,
            destination_station=None,
            api_key=API_KEY
        )

        self.assertTrue(isinstance(response, responses.StationToStationInfos), response)

    @vcr.use_cassette(VCR_STORAGE.format('station_to_station_infos_from_station'))
    def test_station_to_station_from_station(self):
        response = self.requires_station.station_to_station(
            from_station=station.Station["A01"],
            destination_station=None,
            api_key=API_KEY
        )

        self.assertTrue(isinstance(response, responses.StationToStationInfos), response)

    @vcr.use_cassette(VCR_STORAGE.format('station_to_station_infos_destination_station'))
    def test_station_to_station_destination_station(self):
        response = self.requires_station.station_to_station(
            from_station=None,
            destination_station=station.Station["A01"],
            api_key=API_KEY
        )

        self.assertTrue(isinstance(response, responses.StationToStationInfos), response)

    @vcr.use_cassette(VCR_STORAGE.format('station_to_station_infos_both_stations'))
    def test_station_to_station_both_stations(self):
        response = self.requires_station.station_to_station(
            from_station=station.Station["A01"],
            destination_station=station.Station["A02"],
            api_key=API_KEY
        )

        self.assertTrue(isinstance(response, responses.StationToStationInfos), response)


