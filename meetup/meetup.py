import datetime
import calendar

class MeetupDayException(Exception):
    """Thrown when non-existent dates are generated."""
    pass

def meetup_day(yyyy: int, mm: int, dayname: str, position: str) -> datetime.date:
    out = datetime.date(yyyy, mm, 1)

    if position == "teenth":
        out = out + datetime.timedelta(days=12)
    elif position == "1st":
        pass
    elif position == "2nd":
        out = out + datetime.timedelta(days=7)
    elif position == "3rd":
        out = out + datetime.timedelta(days=14)
    elif position == "4th":
        out = out + datetime.timedelta(days=21)
    elif position == "5th":
        out = out + datetime.timedelta(days=28)

    while out.strftime("%A") != dayname:
        out = out + datetime.timedelta(days=1)

    if position == "last":
        lastdate = calendar.monthrange(yyyy, mm)[1]
        out = datetime.date(yyyy, mm, lastdate)
        while out.strftime("%A") != dayname:
            out = out - datetime.timedelta(days=1)

    if int(out.strftime("%-m")) != mm:
        raise MeetupDayException

    return out
