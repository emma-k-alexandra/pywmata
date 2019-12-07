from unittest import TestCase
from datetime import datetime

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

        self.assertIsInstance(station_response.station, station.Station)
    
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

        self.assertIsInstance(
            station_to_station_infos.station_to_station_infos[0], 
            responses.StationToStationInfo
        )

    def test_elevator_and_escalator_incident(self):
        elevator_and_escalator_incident = responses.ElevatorAndEscalatorIncident({
            "DateOutOfServ": "2014-10-27T15:17:00",
            "DateUpdated": "2014-10-28T06:28:30",
            "DisplayOrder": 0,
            "EstimatedReturnToService": "2014-10-30T23:59:59",
            "LocationDescription": "Escalator between mezzanine and platform to Shady Grove",
            "StationCode": "A03",
            "StationName": "Dupont Circle, Q Street Entrance",
            "SymptomCode": None,
            "SymptomDescription": "Service Call",
            "TimeOutOfService": "1517",
            "UnitName": "A03N04",
            "UnitStatus": None,
            "UnitType": "ESCALATOR"
        })

        self.assertIsInstance(
            elevator_and_escalator_incident.estimated_return_to_service, 
            datetime
        )

    def test_elevator_and_escalator_incident_null_return_to_service(self):
        elevator_and_escalator_incident = responses.ElevatorAndEscalatorIncident({
            "DateOutOfServ": "2014-10-27T15:17:00",
            "DateUpdated": "2014-10-28T06:28:30",
            "DisplayOrder": 0,
            "EstimatedReturnToService": None,
            "LocationDescription": "Escalator between mezzanine and platform to Shady Grove",
            "StationCode": "A03",
            "StationName": "Dupont Circle, Q Street Entrance",
            "SymptomCode": None,
            "SymptomDescription": "Service Call",
            "TimeOutOfService": "1517",
            "UnitName": "A03N04",
            "UnitStatus": None,
            "UnitType": "ESCALATOR"
        })

        self.assertEqual(elevator_and_escalator_incident.estimated_return_to_service, None)

    def test_elevator_and_escalator_incidents(self):
        elevator_and_escalator_incidents = responses.ElevatorAndEscalatorIncidents({
            "ElevatorIncidents": [
                {
                    "DateOutOfServ": "2014-10-27T15:17:00",
                    "DateUpdated": "2014-10-28T06:28:30",
                    "DisplayOrder": 0,
                    "EstimatedReturnToService": "2014-10-30T23:59:59",
                    "LocationDescription": "Escalator between mezzanine and platform to Shady Grove",
                    "StationCode": "A03",
                    "StationName": "Dupont Circle, Q Street Entrance",
                    "SymptomCode": None,
                    "SymptomDescription": "Service Call",
                    "TimeOutOfService": "1517",
                    "UnitName": "A03N04",
                    "UnitStatus": None,
                    "UnitType": "ESCALATOR"
                }
            ]
        })

        self.assertIsInstance(
            elevator_and_escalator_incidents.incidents[0],
            responses.ElevatorAndEscalatorIncident
        )

    def test_rail_incident(self):
        rail_incident = responses.RailIncident({
            "DateUpdated": "2010-07-29T14:21:28",
            "DelaySeverity": None,
            "Description": "Red Line: Expect residual delays to Glenmont due to an earlier signal problem outside Forest Glen.",
            "EmergencyText": None,
            "EndLocationFullName": None,
            "IncidentID": "3754F8B2-A0A6-494E-A4B5-82C9E72DFA74",
            "IncidentType": "Delay",
            "LinesAffected": "RD;",
            "PassengerDelay": 0,
            "StartLocationFullName": None
        })

        self.assertIsInstance(rail_incident.date_updated, datetime)

    def test_rail_incidents(self):
        rail_incidents = responses.RailIncidents({
            "Incidents": [
                {
                    "DateUpdated": "2010-07-29T14:21:28",
                    "DelaySeverity": None,
                    "Description": "Red Line: Expect residual delays to Glenmont due to an earlier signal problem outside Forest Glen.",
                    "EmergencyText": None,
                    "EndLocationFullName": None,
                    "IncidentID": "3754F8B2-A0A6-494E-A4B5-82C9E72DFA74",
                    "IncidentType": "Delay",
                    "LinesAffected": "RD;",
                    "PassengerDelay": 0,
                    "StartLocationFullName": None
                }
            ]
        })

        self.assertIsInstance(rail_incidents.incidents[0], responses.RailIncident)

