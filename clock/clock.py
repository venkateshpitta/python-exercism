class Clock(object):
    def __init__(self, hour: int, minute: int) -> None:
        self.hour, self.minute = hour, minute

    def __str__(self) -> str:
        q, r = divmod(self.minute, 60)
        r = r + (0 if r >= 0 else 60)
        h = (self.hour + q) % 24
        h = h + (0 if 0 <= h <= 24 else 24)
        return '{:02d}:{:02d}'.format(h, r)

    def add(self, diff: int) -> str:
        self.minute += diff
        return self.__str__()

    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__) and str(other) == self.__str__()

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
