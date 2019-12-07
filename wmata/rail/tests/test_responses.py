from unittest import TestCase

from wmata.rail import responses, station

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


