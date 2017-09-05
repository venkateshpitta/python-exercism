class Luhn(object):
    def __init__(self, num: str):
        self.cc_num = num.strip().replace(' ', '')

    def is_valid(self) -> bool:
        if not self.cc_num.isdigit() or len(self.cc_num) <= 1: return False
        rev = self.cc_num[::-1]
        odds = [int(rev[r]) for r in range(0, len(rev), 2)]
        evens = [2*int(rev[r]) - (9 if 2*int(rev[r])>9 else 0) for r in range(1, len(rev), 2)]
        return (sum(odds) + sum(evens))%10 == 0
