from typing import List

def detect_anagrams(string: str, array: List[str]) -> List[str]:
    return [x for x in array if x.lower() != string.lower() and sorted(x.lower()) == sorted(string.lower())]
