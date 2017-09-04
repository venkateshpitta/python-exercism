from typing import List

class Allergies(object):

    def __init__(self, number: int):
        self.score = number
        self.table = {1   : 'eggs',
                      2   : 'peanuts',
                      4   : 'shellfish',
                      8   : 'strawberries',
                      16  : 'tomatoes',
                      32  : 'chocolate',
                      64  : 'pollen',
                      128 : 'cats'}

    def is_allergic_to(self, string: str) -> bool:
        return string in self.lst

    @property
    def lst(self) -> List[str]:
        out = []
        for k in self.table.keys():
            if k&self.score == k:
                out.append(self.table[k])
        return out
