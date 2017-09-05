class SpaceAge(object):
    def __init__(self, secs: int):
        self.seconds                  = secs
        self.earth_seconds_per_year   = 31557600
        self.mercury_seconds_per_year = self.earth_seconds_per_year * 0.2408467
        self.venus_seconds_per_year   = self.earth_seconds_per_year * 0.61519726
        self.mars_seconds_per_year    = self.earth_seconds_per_year * 1.8808158
        self.jupiter_seconds_per_year = self.earth_seconds_per_year * 11.862615
        self.saturn_seconds_per_year  = self.earth_seconds_per_year * 29.447498
        self.uranus_seconds_per_year  = self.earth_seconds_per_year * 84.016846
        self.neptune_seconds_per_year = self.earth_seconds_per_year * 164.79132

    def on_earth(self) -> float:
        return round(self.seconds / self.earth_seconds_per_year, 2)

    def on_mercury(self) -> float:
        return round(self.seconds / self.mercury_seconds_per_year, 2)

    def on_venus(self) -> float:
        return round(self.seconds / self.venus_seconds_per_year, 2)

    def on_mars(self) -> float:
        return round(self.seconds / self.mars_seconds_per_year, 2)

    def on_jupiter(self) -> float:
        return round(self.seconds / self.jupiter_seconds_per_year, 2)

    def on_saturn(self) -> float:
        return round(self.seconds / self.saturn_seconds_per_year, 2)

    def on_uranus(self) -> float:
        return round(self.seconds / self.uranus_seconds_per_year, 2)

    def on_neptune(self) -> float:
        return round(self.seconds / self.neptune_seconds_per_year, 2)
