from unittest import TestCase
import vcr

from wmata.rail import mixins, responses, line, station
from .utils import VCR_STORAGE
from ...tests.utils import API_KEY



class TestRequiresLine(TestCase):
    def setUp(self):
        self.requires_line = mixins.RequiresLine()

    @vcr.use_cassette(VCR_STORAGE.format('stations_on'))
    def test_stations_on(self):
        response = self.requires_line._stations_on(
            line=None, 
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.Stations)

    @vcr.use_cassette(VCR_STORAGE.format('stations_on_blue_line'))
    def test_stations_on_blue_line(self):
        response = self.requires_line._stations_on(
            line=line.Line["BL"],
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.Stations)


class TestRequiresStation(TestCase):
    def setUp(self):
        self.requires_station = mixins.RequiresStation()

    @vcr.use_cassette(VCR_STORAGE.format('station_to_station_infos'))
    def test_station_to_station(self):
        response = self.requires_station._station_to_station(
            from_station=None,
            destination_station=None,
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.StationToStationInfos)

    @vcr.use_cassette(VCR_STORAGE.format('station_to_station_infos_from_station'))
    def test_station_to_station_from_station(self):
        response = self.requires_station._station_to_station(
            from_station=station.Station["A01"],
            destination_station=None,
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.StationToStationInfos)

    @vcr.use_cassette(VCR_STORAGE.format('station_to_station_infos_destination_station'))
    def test_station_to_station_destination_station(self):
        response = self.requires_station._station_to_station(
            from_station=None,
            destination_station=station.Station["A01"],
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.StationToStationInfos)

    @vcr.use_cassette(VCR_STORAGE.format('station_to_station_infos_both_stations'))
    def test_station_to_station_both_stations(self):
        response = self.requires_station._station_to_station(
            from_station=station.Station["A01"],
            destination_station=station.Station["A02"],
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.StationToStationInfos)

    @vcr.use_cassette(VCR_STORAGE.format('elevator_and_escalator_incidents'))
    def test_elevator_and_escalator_incidents(self):
        response = self.requires_station._elevator_and_escalator_incidents_at(
            station=None,
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.ElevatorAndEscalatorIncidents)

    @vcr.use_cassette(VCR_STORAGE.format('elevator_and_escalator_incidents_A01'))
    def test_elevator_and_escalator_incidents_at_metro_center(self):
        response = self.requires_station._elevator_and_escalator_incidents_at(
            station=station.Station["A01"],
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.ElevatorAndEscalatorIncidents)

    @vcr.use_cassette(VCR_STORAGE.format('rail_incidents'))
    def test_rail_incidents(self):
        response = self.requires_station._incidents_at(
            station=None,
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.RailIncidents)

    @vcr.use_cassette(VCR_STORAGE.format('rail_incidents_at_station'))
    def test_rail_incidents_at_station(self):
        response = self.requires_station._incidents_at(
            station=station.Station["A01"],
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.RailIncidents)

    @vcr.use_cassette(VCR_STORAGE.format('next_trains'))
    def test_next_trains(self):
        response = self.requires_station._next_trains(
            station=station.Station["A01"],
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.RailPredictions)

    @vcr.use_cassette(VCR_STORAGE.format('station_information'))
    def test_station_information(self):
        response = self.requires_station._station_information(
            station=station.Station["A01"],
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.StationInformation)

    @vcr.use_cassette(VCR_STORAGE.format('stations_parking'))
    def test_stations_parking(self):
        response = self.requires_station._parking_information(
            station=station.Station["A01"],
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.StationsParking)

    @vcr.use_cassette(VCR_STORAGE.format('timings'))
    def test_timings(self):
        response = self.requires_station._timings(
            station=station.Station["A01"],
            api_key=API_KEY
        )

        self.assertIsInstance(response, responses.StationTimings)
