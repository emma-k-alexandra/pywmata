from datetime import datetime

DATE_FORMAT = r"%Y-%m-%dT%H:%M:%S"

def string_to_datetime(string: str) -> datetime:
    return datetime.strptime(string, DATE_FORMAT)

class Date:
    year: int
    month: int
    day: int

    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        return "{:04d}-{:02d}-{:02d}".format(self.year, self.month, self.day)
        