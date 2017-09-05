from typing import List

class Garden(object):
    def __init__(self, cups:str, students: List[str] = "Alice Bob Charlie \
David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry".split()):
        self.rows = cups.split('\n')
        self.students = students

    def plants(self, kid: str) -> List[str]:
        start = 2 * self.students.index(kid)
        four = {"V": "Violets", "R": "Radishes", "C": "Clover", "G": "Grass"}
        return [four[p] for p in
                [self.rows[0][start],
                 self.rows[0][start+1],
                 self.rows[1][start],
                 self.rows[1][start+1]]]
