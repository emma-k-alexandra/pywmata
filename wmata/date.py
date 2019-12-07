from datetime import datetime

DATE_FORMAT = r"%Y-%m-%dT%H:%M:%S"

def string_to_datetime(string: str) -> datetime:
    return datetime.strptime(string, DATE_FORMAT)