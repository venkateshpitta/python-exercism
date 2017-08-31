from datetime import datetime
from datetime import timedelta

def add_gigasecond(start: datetime) -> datetime:
    return start + timedelta(seconds=10**9)
