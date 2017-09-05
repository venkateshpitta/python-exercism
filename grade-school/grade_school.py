from typing import Tuple, Sequence

class School(object):
    def __init__(self, schoolname: str):
        self.schoolname = schoolname
        self.register = dict()

    def add(self, student_name: str, grade: int) -> None:
        self.register.setdefault(grade, []).append(student_name)

    def grade(self, g: int) -> Tuple[str]:
        return self.register.get(g, [])

    def sort(self) -> Sequence[str]:
        return [(g, tuple(sorted(self.register[g]))) for g in sorted(self.register)]
