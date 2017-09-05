from typing import Dict, List

def transform(given: Dict[int, List[str]]) -> Dict[str, int]:
    out = dict()
    for score, letters in given.items():
        for letter in letters:
            out[letter.lower()] = score

    return out
