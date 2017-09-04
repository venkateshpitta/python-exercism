NORTH, EAST, SOUTH, WEST = (0, 1), (1, 0), (0, -1), (-1, 0)

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def turn_right(self):
        self.bearing = {NORTH: EAST,
                        EAST: SOUTH,
                        SOUTH: WEST,
                        WEST: NORTH}[self.bearing]

    def turn_left(self):
        self.bearing = {NORTH: WEST,
                        WEST: SOUTH,
                        SOUTH: EAST,
                        EAST: NORTH}[self.bearing]

    def advance(self):
        self.coordinates = tuple(c1+c2 for c1,c2 in zip(self.coordinates,
                                                        self.bearing))

    def simulate(self, directions):
        for d in directions:
            {'L': self.turn_left,
             'R': self.turn_right,
             'A': self.advance}[d]()
