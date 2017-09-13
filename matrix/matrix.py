class Matrix(object):
    def __init__(self, given: str):
        self.given = given
        self.rows = [[int(i) for i in row.split()] for row in self.given.split('\n')]
        self.columns = [list(r) for r in zip(*self.rows)]
