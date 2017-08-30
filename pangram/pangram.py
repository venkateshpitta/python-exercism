import re

def is_pangram(given: str) -> bool:
    temp = re.sub(r'[^a-zA-Z]', '', given).lower()
    return len(set(temp)) == 26
