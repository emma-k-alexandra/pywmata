from unittest import TestCase
from datetime import datetime

from wmata.rail import responses, station, line

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

    def test_rail_prediction(self):
        rail_prediction = responses.RailPrediction({
            "Car": "8",
            "Destination": "Glenmont",
            "DestinationCode": "B11",
            "DestinationName": "Glenmont",
            "Group": "1",
            "Line": "RD",
            "LocationCode": "B03",
            "LocationName": "Union Station",
            "Min": "3"
        })

        self.assertIsInstance(rail_prediction.destination_station, station.Station)

    def test_rail_predictions(self):
        rail_predictions = responses.RailPredictions({
            "Trains": [{
                "Car": "8",
                "Destination": "Glenmont",
                "DestinationCode": "B11",
                "DestinationName": "Glenmont",
                "Group": "1",
                "Line": "RD",
                "LocationCode": "B03",
                "LocationName": "Union Station",
                "Min": "3"
            }]})

        self.assertIsInstance(rail_predictions.trains[0], responses.RailPrediction)

    def test_station_information(self):
        station_information = responses.StationInformation({
            "Address": {
                "City": "Washington",
                "State": "DC",
                "Street": "607 13th St. NW",
                "Zip": "20005"
            },
            "Code": "A01",
            "Lat": 38.8983144732,
            "LineCode1": "RD",
            "LineCode2": None,
            "LineCode3": None,
            "LineCode4": None,
            "Lon": -77.0280779971,
            "Name": "Metro Center",
            "StationTogether1": "C01",
            "StationTogether2": ""
        })

        self.assertIsInstance(station_information.first_station_together, station.Station)

    def test_short_term_parking(self):
        short_term_parking = responses.ShortTermParking({
            "TotalCount": 15,
            "Notes": "Short term parking available 5 am - 2 am, time limit 12 hours"
        })

        self.assertEqual(short_term_parking.total_count, 15)

    def test_all_day_parking(self):
        all_day_parking = responses.AllDayParking({
            "TotalCount": 808,
            "RiderCost": 4.45,
            "NonRiderCost": 4.45,
            "SaturdayRiderCost": 2,
            "SaturdayNonRiderCost": 2,
        })

        self.assertEqual(all_day_parking.total_count, 808)

    def test_station_parking(self):
        station_parking = responses.StationParking({
            "Code": "F06",
            "Notes": "325 spaces metered for 12-hr. max. @ $1.00 per 60 mins.",
            "AllDayParking": {
                "TotalCount": 808,
                "RiderCost": 4.45,
                "NonRiderCost": 4.45,
                "SaturdayRiderCost": 2,
                "SaturdayNonRiderCost": 2,
            },
            "ShortTermParking": {
                "TotalCount": 15,
                "Notes": "Short term parking available 5 am - 2 am, time limit 12 hours"
            }
        })

        self.assertIsInstance(station_parking.all_day_parking, responses.AllDayParking)

    def test_stations_parking(self):
        stations_parking = responses.StationsParking({
            "StationsParking": [
                {
                    "Code": "F06",
                    "Notes": "325 spaces metered for 12-hr. max. @ $1.00 per 60 mins.",
                    "AllDayParking": {
                        "TotalCount": 808,
                        "RiderCost": 4.45,
                        "NonRiderCost": 4.45,
                        "SaturdayRiderCost": 2,
                        "SaturdayNonRiderCost": 2,
                    },
                    "ShortTermParking": {
                        "TotalCount": 15,
                        "Notes": "Short term parking available 5 am - 2 am, time limit 12 hours"
                    }
                }
            ]
        })

        self.assertIsInstance(stations_parking.stations_parking[0], responses.StationParking)

    def test_path(self):
        path = responses.Path({
            "DistanceToPrev": 0,
            "LineCode": "SV",
            "SeqNum": 1,
            "StationCode": "N06",
            "StationName": "Wiehle-Reston East"
        })

        self.assertEqual(path.line, line.Line["SV"])

    def test_path_between_stations(self):
        path_between_stations = responses.PathBetweenStations({
            "Path": [
                {
                    "DistanceToPrev": 0,
                    "LineCode": "SV",
                    "SeqNum": 1,
                    "StationCode": "N06",
                    "StationName": "Wiehle-Reston East"
                }
            ]
        })

        self.assertIsInstance(path_between_stations.path[0], responses.Path)

    def test_train_time(self):
        train_time = responses.TrainTime({
            "Time": "05:00",
            "DestinationStation": "F11"
        })

        self.assertEqual(train_time.destination, station.Station["F11"])

    def test_station_first_last_trains(self):
        station_first_last_trains = responses.StationFirstLastTrains({
            "OpeningTime": "04:50",
            "FirstTrains": [
                {
                    "Time": "05:00",
                    "DestinationStation": "F11"
                }
            ],
            "LastTrains": [
                {
                    "Time": "23:30",
                    "DestinationStation": "F11"
                }
            ]
        })

        self.assertIsInstance(station_first_last_trains.first_trains[0], responses.TrainTime)

    def test_station_time(self):
        station_time = responses.StationTime({
            "Code": "E10",
            "StationName": "Greenbelt",
            "Monday": {
                "OpeningTime": "04:50",
                "FirstTrains": [
                    {
                        "Time": "05:00",
                        "DestinationStation": "F11"
                    }
                ],
                "LastTrains": [
                    {
                        "Time": "23:30",
                        "DestinationStation": "F11"
                    }
                ]
            },
            "Tuesday": {
                "OpeningTime": "04:50",
                "FirstTrains": [
                    {
                        "Time": "05:00",
                        "DestinationStation": "F11"
                    }
                ],
                "LastTrains": [
                    {
                        "Time": "23:30",
                        "DestinationStation": "F11"
                    }
                ]
            },
            "Wednesday": {
                "OpeningTime": "04:50",
                "FirstTrains": [
                    {
                        "Time": "05:00",
                        "DestinationStation": "F11"
                    }
                ],
                "LastTrains": [
                    {
                        "Time": "23:30",
                        "DestinationStation": "F11"
                    }
                ]
            },
            "Thursday": {
                "OpeningTime": "04:50",
                "FirstTrains": [
                    {
                        "Time": "05:00",
                        "DestinationStation": "F11"
                    }
                ],
                "LastTrains": [
                    {
                        "Time": "23:30",
                        "DestinationStation": "F11"
                    }
                ]
            },
            "Friday": {
                "OpeningTime": "04:50",
                "FirstTrains": [
                    {
                        "Time": "05:00",
                        "DestinationStation": "F11"
                    }
                ],
                "LastTrains": [
                    {
                        "Time": "02:30",
                        "DestinationStation": "F11"
                    }
                ]
            },
            "Saturday": {
                "OpeningTime": "06:50",
                "FirstTrains": [
                    {
                        "Time": "07:00",
                        "DestinationStation": "F11"
                    }
                ],
                "LastTrains": [
                    {
                        "Time": "02:30",
                        "DestinationStation": "F11"
                    }
                ]
            },
            "Sunday": {
                "OpeningTime": "06:50",
                "FirstTrains": [
                    {
                        "Time": "07:00",
                        "DestinationStation": "F11"
                    }
                ],
                "LastTrains": [
                    {
                        "Time": "23:30",
                        "DestinationStation": "F11"
                    }
                ]
            }
        })

        self.assertIsInstance(station_time.monday, responses.StationFirstLastTrains)

    def test_station_timings(self):
        station_timings = responses.StationTimings({
            "StationTimes": [
                {
                    "Code": "E10",
                    "StationName": "Greenbelt",
                    "Monday": {
                        "OpeningTime": "04:50",
                        "FirstTrains": [
                            {
                                "Time": "05:00",
                                "DestinationStation": "F11"
                            }
                        ],
                        "LastTrains": [
                            {
                                "Time": "23:30",
                                "DestinationStation": "F11"
                            }
                        ]
                    },
                    "Tuesday": {
                        "OpeningTime": "04:50",
                        "FirstTrains": [
                            {
                                "Time": "05:00",
                                "DestinationStation": "F11"
                            }
                        ],
                        "LastTrains": [
                            {
                                "Time": "23:30",
                                "DestinationStation": "F11"
                            }
                        ]
                    },
                    "Wednesday": {
                        "OpeningTime": "04:50",
                        "FirstTrains": [
                            {
                                "Time": "05:00",
                                "DestinationStation": "F11"
                            }
                        ],
                        "LastTrains": [
                            {
                                "Time": "23:30",
                                "DestinationStation": "F11"
                            }
                        ]
                    },
                    "Thursday": {
                        "OpeningTime": "04:50",
                        "FirstTrains": [
                            {
                                "Time": "05:00",
                                "DestinationStation": "F11"
                            }
                        ],
                        "LastTrains": [
                            {
                                "Time": "23:30",
                                "DestinationStation": "F11"
                            }
                        ]
                    },
                    "Friday": {
                        "OpeningTime": "04:50",
                        "FirstTrains": [
                            {
                                "Time": "05:00",
                                "DestinationStation": "F11"
                            }
                        ],
                        "LastTrains": [
                            {
                                "Time": "02:30",
                                "DestinationStation": "F11"
                            }
                        ]
                    },
                    "Saturday": {
                        "OpeningTime": "06:50",
                        "FirstTrains": [
                            {
                                "Time": "07:00",
                                "DestinationStation": "F11"
                            }
                        ],
                        "LastTrains": [
                            {
                                "Time": "02:30",
                                "DestinationStation": "F11"
                            }
                        ]
                    },
                    "Sunday": {
                        "OpeningTime": "06:50",
                        "FirstTrains": [
                            {
                                "Time": "07:00",
                                "DestinationStation": "F11"
                            }
                        ],
                        "LastTrains": [
                            {
                                "Time": "23:30",
                                "DestinationStation": "F11"
                            }
                        ]
                    }
                }
            ]
        })

        self.assertIsInstance(station_timings.station_times[0], responses.StationTime)
    
    def test_line_response(self):
        line_response = responses.LineResponse({
            "DisplayName": "Green",
            "EndStationCode": "E10",
            "InternalDestination1": "",
            "InternalDestination2": "",
            "LineCode": "GR",
            "StartStationCode": "F11"
        })

        self.assertEqual(line_response.end_station, station.Station["E10"])

    def test_lines(self):
        lines = responses.Lines({
            "Lines": [
                {
                    "DisplayName": "Green",
                    "EndStationCode": "E10",
                    "InternalDestination1": "",
                    "InternalDestination2": "",
                    "LineCode": "GR",
                    "StartStationCode": "F11"
                },
                {
                    "DisplayName": "Blue",
                    "EndStationCode": "G05",
                    "InternalDestination1": "",
                    "InternalDestination2": "",
                    "LineCode": "BL",
                    "StartStationCode": "J03"
                },
                {
                    "DisplayName": "Silver",
                    "EndStationCode": "G05",
                    "InternalDestination1": "",
                    "InternalDestination2": "",
                    "LineCode": "SV",
                    "StartStationCode": "N06"
                },
                {
                    "DisplayName": "Red",
                    "EndStationCode": "B11",
                    "InternalDestination1": "A11",
                    "InternalDestination2": "B08",
                    "LineCode": "RD",
                    "StartStationCode": "A15"
                },
                {
                    "DisplayName": "Orange",
                    "EndStationCode": "D13",
                    "InternalDestination1": "",
                    "InternalDestination2": "",
                    "LineCode": "OR",
                    "StartStationCode": "K08"
                },
                {
                    "DisplayName": "Yellow",
                    "EndStationCode": "E06",
                    "InternalDestination1": "E01",
                    "InternalDestination2": "",
                    "LineCode": "YL",
                    "StartStationCode": "C15"
                }
            ]
        })

        self.assertIsInstance(lines.lines[0], responses.LineResponse)

    def test_station_entrance(self):
        station_entrance = responses.StationEntrance({
            "Description": "Farragut West, 17th & I St",
            "ID": "100",
            "Lat": 38.901098,
            "Lon": -77.039293,
            "Name": "Farragut West 17th & I St",
            "StationCode1": "C03",
            "StationCode2": ""
        })

        self.assertEqual(station_entrance.first_station, station.Station["C03"])

    def test_station_entrances(self):
        station_entrances = responses.StationEntrances({
            "Entrances": [
                {
                    "Description": "Farragut West, 17th & I St",
                    "ID": "100",
                    "Lat": 38.901098,
                    "Lon": -77.039293,
                    "Name": "Farragut West 17th & I St",
                    "StationCode1": "C03",
                    "StationCode2": ""
                },
                {
                    "Description": "Farragut West, 18th & I St",
                    "ID": "101",
                    "Lat": 38.901453,
                    "Lon": -77.042093,
                    "Name": "Farragut West 18th & I St",
                    "StationCode1": "C03",
                    "StationCode2": ""
                }
            ]
        })

        self.assertIsInstance(station_entrances.entrances[0], responses.StationEntrance)

    def test_train_position(self):
        train_position = responses.TrainPosition({
            "TrainId": "100",
            "TrainNumber": "301",
            "CarCount": 6,
            "DirectionNum": 1,
            "CircuitId": 1234,
            "DestinationStationCode": "A01",
            "LineCode": "RD",
            "SecondsAtLocation": 0,
            "ServiceType": "Normal"    
        })

        self.assertEqual(train_position.line, line.Line["RD"])

    def test_train_positions(self):
        train_positions = responses.TrainPositions({
            "TrainPositions":[
                {
                    "TrainId": "100",
                    "TrainNumber": "301",
                    "CarCount": 6,
                    "DirectionNum": 1,
                    "CircuitId": 1234,
                    "DestinationStationCode": "A01",
                    "LineCode": "RD",
                    "SecondsAtLocation": 0,
                    "ServiceType": "Normal"    
                },
                {
                    "TrainId": "200",
                    "TrainNumber": "XY1",
                    "CarCount": 6,
                    "DirectionNum": 2,
                    "CircuitId": 4321,
                    "DestinationStationCode": None,
                    "LineCode": None,
                    "SecondsAtLocation": 25,
                    "ServiceType": "Special"
                }
            ]
        })

        self.assertIsInstance(train_positions.train_positions[0], responses.TrainPosition)

    def test_track_circuit_with_station(self):
        track_circuit_with_station = responses.TrackCircuitWithStation({
            "SeqNum": 0,
            "CircuitId": 2603,
            "StationCode": None
        })

        self.assertEqual(track_circuit_with_station.sequence_number, 0)

    def test_standard_route(self):
        standard_route = responses.StandardRoute({
            "LineCode": "YLRP",
            "TrackNum": 2,
            "TrackCircuits": []
        })

        self.assertEqual(standard_route.line, line.Line["YLRP"])

    def test_standard_routes(self):
        standard_routes = responses.StandardRoutes({
            "StandardRoutes": [
                {
                    "LineCode": "YLRP",
                    "TrackNum": 2,
                    "TrackCircuits": []
                }
            ]
        })

        self.assertIsInstance(standard_routes.standard_routes[0], responses.StandardRoute)

    def test_track_neighbor(self):
        track_neighbor = responses.TrackNeighbor({
            "NeighborType": "Right",
            "CircuitIds": [4, 3]
        })

        self.assertEqual(track_neighbor.circuit_ids, [4, 3])

    def test_track_circuit(self):
        track_circuit = responses.TrackCircuit({
            "Track": 2,
            "CircuitId": 8,
            "Neighbors": [
                {
                    "NeighborType": "Right",
                    "CircuitIds": [4, 3]
                }
            ]
        })

        self.assertIsInstance(track_circuit.neighbors[0], responses.TrackNeighbor)

    def test_track_circuits(self):
        track_circuits = responses.TrackCircuits({
            "TrackCircuits": [
                {
                    "Track": 2,
                    "CircuitId": 8,
                    "Neighbors": [
                        {
                            "NeighborType": "Right",
                            "CircuitIds": [4, 3]
                        }
                    ]
                }
            ]
        })

        self.assertIsInstance(track_circuits.track_circuits[0], responses.TrackCircuit)
    