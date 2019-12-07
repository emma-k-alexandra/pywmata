from unittest import TestCase

from wmata.rail import responses, station
from wmata.rail import station

class TestResponses(TestCase):
    def test_address(self):
        address = responses.Address({
            "City": "Rockville",
            "State": "MD",
            "Street": "15903 Somerville Drive",
            "Zip": "20855"
        })

        self.assertEqual(address.city, "Rockville")

    def test_station_response(self):
        station_response = responses.StationResponse({
            "Address": {
                "City": "Rockville",
                "State": "MD",
                "Street": "15903 Somerville Drive",
                "Zip": "20855"
            },
            "Code": "A15",
            "Lat": 39.1199273249,
            "LineCode1": "RD",
            "LineCode2": None,
            "LineCode3": None,
            "LineCode4": None,
            "Lon": -77.1646273343,
            "Name": "Shady Grove",
            "StationTogether1": "",
            "StationTogether2": ""
        })

        self.assertTrue(isinstance(station_response.station, station.Station))
    
    def test_stations(self):
        stations = responses.Stations({
            "Stations": [
                {
                    "Address": {
                        "City": "Rockville",
                        "State": "MD",
                        "Street": "15903 Somerville Drive",
                        "Zip": "20855"
                    },
                    "Code": "A15",
                    "Lat": 39.1199273249,
                    "LineCode1": "RD",
                    "LineCode2": None,
                    "LineCode3": None,
                    "LineCode4": None,
                    "Lon": -77.1646273343,
                    "Name": "Shady Grove",
                    "StationTogether1": "",
                    "StationTogether2": ""
                }
            ]
        })

        self.assertTrue(isinstance(stations.stations[0], responses.StationResponse))

    def test_rail_fare(self):
        rail_fare = responses.RailFare({
            "OffPeakTime": 3.6,
            "PeakTime": 5.9,
            "SeniorDisabled": 2.95
        })

        self.assertEqual(rail_fare.peak_time, 5.9)

    def test_station_to_station_info(self):
        station_to_station_info = responses.StationToStationInfo({
            "CompositeMiles": 25.41,
            "DestinationStation": "J03",
            "RailFare": {
                "OffPeakTime": 3.6,
                "PeakTime": 5.9,
                "SeniorDisabled": 2.95
            },
            "RailTime": 66,
            "SourceStation": "E10"
        })

        self.assertEqual(station_to_station_info.source, station.Station["E10"])

    def test_station_to_station_infos(self):
        station_to_station_infos = responses.StationToStationInfos({
            "StationToStationInfos": [
                {
                    "CompositeMiles": 25.41,
                    "DestinationStation": "J03",
                    "RailFare": {
                        "OffPeakTime": 3.6,
                        "PeakTime": 5.9,
                        "SeniorDisabled": 2.95
                    },
                    "RailTime": 66,
                    "SourceStation": "E10"
                }
            ]
        })

        self.assertTrue(isinstance(
            station_to_station_infos.station_to_station_infos[0], 
            responses.StationToStationInfo
        ))