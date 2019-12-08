class Coordinates:
    latitude: float
    longitude: float

    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

class RadiusAtCoordinates:
    radius: int
    coordinates: Coordinates

    def __init__(self, radius: int, coordinates: Coordinates):
        self.radius = radius
        self.coordinates = coordinates

    def to_dict(self):
        return {
            "Radius": self.radius,
            "Lat": self.coordinates.latitude,
            "Lon": self.coordinates.longitude
        }
