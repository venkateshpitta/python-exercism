import re

def is_isogram(string: str) -> bool:
    temp = re.sub(r'[^a-zA-Z]', '', string.lower())
    return len(temp)==len(set(temp))
