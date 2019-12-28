from unittest import TestCase
from datetime import datetime
from wmata.bus import responses, route, stop

class TestResponses(TestCase):
    def test_bus_position(self):
        bus_position = responses.BusPosition({
            "DateTime": "2014-10-27T13:23:40",
            "Deviation": 7,
            "DirectionNum": "10",
            "DirectionText": "NORTH",
            "Lat": 39.191525,
            "Lon": -76.672821,
            "RouteID": "B30",
            "TripEndTime": "2014-10-27T13:17:00",
            "TripHeadsign": "BWI LT RAIL STA",
            "TripID": "6794838",
            "TripStartTime": "2014-10-27T12:40:00",
            "VehicleID": "6217"
        })

        self.assertEqual(bus_position.trip_id, "6794838")

    def test_bus_positions(self):
        bus_positions = responses.BusPositions({
            "BusPositions": [
                {
                    "DateTime": "2014-10-27T13:23:40",
                    "Deviation": 7,
                    "DirectionNum": "10",
                    "DirectionText": "NORTH",
                    "Lat": 39.191525,
                    "Lon": -76.672821,
                    "RouteID": "B30",
                    "TripEndTime": "2014-10-27T13:17:00",
                    "TripHeadsign": "BWI LT RAIL STA",
                    "TripID": "6794838",
                    "TripStartTime": "2014-10-27T12:40:00",
                    "VehicleID": "6217"
                }
            ]
        })

        self.assertIsInstance(
            bus_positions.bus_positions[0], 
            responses.BusPosition
        )

    def test_incident(self):
        incident = responses.Incident({
            "DateUpdated": "2014-10-28T08:13:03",
            "Description": "90, 92, X1, X2, X9: Due to traffic congestion at 8th & H St NE, buses are experiencing up to 20 minute delays in both directions.",
            "IncidentID": "32297013-57B6-467F-BC6B-93DFA4115652",
            "IncidentType": "Delay",
            "RoutesAffected": [
                "90",
                "92",
                "X1",
                "X2",
                "X9"
            ]
        })

        self.assertEqual(incident.incident_id, "32297013-57B6-467F-BC6B-93DFA4115652")

    def test_incidents(self):
        incidents = responses.Incidents({
            "BusIncidents": [
                {
                    "DateUpdated": "2014-10-28T08:13:03",
                    "Description": "90, 92, X1, X2, X9: Due to traffic congestion at 8th & H St NE, buses are experiencing up to 20 minute delays in both directions.",
                    "IncidentID": "32297013-57B6-467F-BC6B-93DFA4115652",
                    "IncidentType": "Delay",
                    "RoutesAffected": [
                        "90",
                        "92",
                        "X1",
                        "X2",
                        "X9"
                    ]
                }
            ]
        })

        self.assertIsInstance(incidents.incidents[0], responses.Incident)

    def test_path_shape(self):
        path_stop = responses.PathShape({
            "Lat": 39.011595754,
            "Lon": -76.909996671,
            "SeqNum": 1
        })

        self.assertEqual(path_stop.latitude, 39.011595754)

    def test_stop_routes(self):
        stop_routes = responses.StopRoutes({
            "Lat": 39.011724,
            "Lon": -76.910024,
            "Name": "GREENBELT STATION + BUS BAY D",
            "Routes": [
                "B30"
            ],
            "StopID": "3003037"
        })

        self.assertIsInstance(stop_routes.routes[0], route.Route)

    def test_path_direction(self):
        path_direction = responses.PathDirection({
            "DirectionNum": "0",
            "DirectionText": "NORTH",
            "Shape": [
                {
                    "Lat": 39.011595754,
                    "Lon": -76.909996671,
                    "SeqNum": 1
                }
            ],
            "Stops": [
                {
                    "Lat": 39.011724,
                    "Lon": -76.910024,
                    "Name": "GREENBELT STATION + BUS BAY D",
                    "Routes": [
                        "B30"
                    ],
                    "StopID": "3003037"
                }
            ],
            "TripHeadsign": "BWI - THURGOOD MARSHALL  AIRPORT"
        })

        self.assertIsInstance(path_direction.stops[0], responses.StopRoutes)

    def test_path_details(self):
        path_details = responses.PathDetails({
            "RouteID": "B30",
            "Name": "B30 - B30 GREENBELT-BWI (647)",
            "Direction0": {
                "DirectionNum": "0",
                "DirectionText": "NORTH",
                "Shape": [
                    {
                        "Lat": 39.011595754,
                        "Lon": -76.909996671,
                        "SeqNum": 1
                    }
                ],
                "Stops": [
                    {
                        "Lat": 39.011724,
                        "Lon": -76.910024,
                        "Name": "GREENBELT STATION + BUS BAY D",
                        "Routes": [
                            "B30"
                        ],
                        "StopID": "3003037"
                    }
                ],
                "TripHeadsign": "BWI - THURGOOD MARSHALL  AIRPORT"
            },
            "Direction1": None
        })

        self.assertIsInstance(path_details.direction_zero, responses.PathDirection)
        self.assertEqual(path_details.direction_one, None)

    def test_stop_info(self):
        stop_info = responses.StopInfo({
            "StopID": "3003037",
            "StopName": "GREENBELT STATION + BUS BAY D",
            "StopSeq": 1,
            "Time": "2014-10-27T06:10:00"
        })

        self.assertIsInstance(stop_info.stop, stop.Stop)

    def test_route_info(self):
        route_info = responses.RouteInfo({
            "DirectionNum": "0",
            "EndTime": "2014-10-27T06:45:00",
            "RouteID": "B30",
            "StartTime": "2014-10-27T06:10:00",
            "StopTimes": [
                {
                    "StopID": "3003037",
                    "StopName": "GREENBELT STATION + BUS BAY D",
                    "StopSeq": 1,
                    "Time": "2014-10-27T06:10:00"
                }
            ],
            "TripDirectionText": "NORTH",
            "TripHeadsign": "BWI - THURGOOD MARSHALL  AIRPORT",
            "TripID": "6794828"
        })

        self.assertIsInstance(route_info.end_time, datetime)

    def test_route_schedule(self):
        route_schedule = responses.RouteSchedule({
            "Direction0": [{
                "DirectionNum": "0",
                "EndTime": "2014-10-27T06:45:00",
                "RouteID": "B30",
                "StartTime": "2014-10-27T06:10:00",
                "StopTimes": [
                    {
                        "StopID": "3003037",
                        "StopName": "GREENBELT STATION + BUS BAY D",
                        "StopSeq": 1,
                        "Time": "2014-10-27T06:10:00"
                    }
                ],
                "TripDirectionText": "NORTH",
                "TripHeadsign": "BWI - THURGOOD MARSHALL  AIRPORT",
                "TripID": "6794828"
            }],
            "Direction1": [{
                "DirectionNum": "0",
                "EndTime": "2014-10-27T06:45:00",
                "RouteID": "B30",
                "StartTime": "2014-10-27T06:10:00",
                "StopTimes": [
                    {
                        "StopID": "3003037",
                        "StopName": "GREENBELT STATION + BUS BAY D",
                        "StopSeq": 1,
                        "Time": "2014-10-27T06:10:00"
                    }
                ],
                "TripDirectionText": "NORTH",
                "TripHeadsign": "BWI - THURGOOD MARSHALL  AIRPORT",
                "TripID": "6794828"
            }],
            "Name": "B30 - B30 GREENBELT-BWI (647)"
        })

        self.assertIsInstance(route_schedule.direction_zero[0], responses.RouteInfo)

    def test_prediction(self):
        prediction = responses.Prediction({
            "DirectionNum": "0",
            "DirectionText": "North to Bwi - Thurgood Marshall Airport",
            "Minutes": 8,
            "RouteID": "B30",
            "TripID": "6794838",
            "VehicleID": "6217"
        })

        self.assertIsInstance(prediction.route, route.Route)

    def test_predictions(self):
        predictions = responses.Predictions({
            "Predictions": [
                {
                    "DirectionNum": "0",
                    "DirectionText": "North to Bwi - Thurgood Marshall Airport",
                    "Minutes": 8,
                    "RouteID": "B30",
                    "TripID": "6794838",
                    "VehicleID": "6217"
                }
            ]
        })

        self.assertIsInstance(predictions.predictions[0], responses.Prediction)

    def test_arrival(self):
        arrival = responses.Arrival({
            "DirectionNum": "1",
            "EndTime": "2014-10-27T05:37:00",
            "RouteID": "87c",
            "ScheduleTime": "2014-10-27T05:35:12",
            "StartTime": "2014-10-27T04:46:00",
            "TripDirectionText": "SOUTH",
            "TripHeadsign": "GREENBELT STATION",
            "TripID": "6788790"
        })

        self.assertIsInstance(arrival.route, route.Route)

    def test_stop_schedule(self):
        stop_schedule = responses.StopSchedule({
            "ScheduleArrivals": [
                {
                    "DirectionNum": "1",
                    "EndTime": "2014-10-27T05:37:00",
                    "RouteID": "87c",
                    "ScheduleTime": "2014-10-27T05:35:12",
                    "StartTime": "2014-10-27T04:46:00",
                    "TripDirectionText": "SOUTH",
                    "TripHeadsign": "GREENBELT STATION",
                    "TripID": "6788790"
                }
            ],
            "Stop": {
                "Lat": 39.011425,
                "Lon": -76.904307,
                "Name": "GREENBELT METRO DR + CHERRYWOOD LA",
                "Routes": [
                    "81",
                    "87",
                    "87c",
                    "87cv1",
                    "89",
                    "89M",
                    "89v1",
                    "B30",
                    "C2",
                    "G12",
                    "G13",
                    "G14",
                    "G16",
                    "G16v1",
                    "R11",
                    "R12",
                    "R3"
                ],
                "StopID": "3002578"
            }
        })

        self.assertIsInstance(stop_schedule.stop, responses.StopRoutes)

    def test_route_response(self):
        route_response = responses.RouteResponse({
            "RouteID": "10A",
            "Name": "10A - HUNTING POINT -PENTAGON",
            "LineDescription": "Hunting Point-Pentagon Line"
		})

        self.assertIsInstance(route_response.route, route.Route)

    def test_routes(self):
        routes = responses.Routes({  
            "Routes": [
                {
                    "RouteID": "10A",
                    "Name": "10A - HUNTING POINT -PENTAGON",
                    "LineDescription": "Hunting Point-Pentagon Line"
                },
                {
                    "RouteID": "10Av1",
                    "Name": "10A - PENDELTON+COLUMBUS-PENTAGON",
                    "LineDescription": "Hunting Point-Pentagon Line"
                },
                {
                    "RouteID": "10B",
                    "Name": "10B - HUNTING POINT - BALLSTON STA",
                    "LineDescription": "Hunting Point-Ballston Line"
                },
                {
                    "RouteID": "10Bc",
                    "Name": "10B - BALLSTON STA - PENDLETON+COLUMBS",
                    "LineDescription": "Hunting Point-Ballston Line"
                }
            ]
        })

        self.assertIsInstance(routes.routes[0], responses.RouteResponse)

    def test_stop_response(self):
        stop_response = responses.StopResponse({
            "Lat": 38.878356,
            "Lon": -76.990378,
            "Name": "K ST + POTOMAC AVE",
            "Routes": [
                "V7",
                "V7c",
                "V7cv1",
                "V7v1",
                "V7v2",
                "V8",
                "V9"
            ],
            "StopID": "1000533"
        })

        self.assertIsInstance(stop_response.stop, stop.Stop)

    def test_stops(self):
        stops = responses.Stops({
            "Stops": [
                {
                    "Lat": 38.878356,
                    "Lon": -76.990378,
                    "Name": "K ST + POTOMAC AVE",
                    "Routes": [
                        "V7",
                        "V7c",
                        "V7cv1",
                        "V7v1",
                        "V7v2",
                        "V8",
                        "V9"
                    ],
                    "StopID": "1000533"
                }
            ]
        })

        self.assertIsInstance(stops.stops[0], responses.StopResponse)
