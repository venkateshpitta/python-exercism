import math

def encode(given: str) -> str:
    if len(given)==0: return given
    cleansed = [g for g in given.lower() if g.isalnum()]
    width = int(math.ceil(len(cleansed)**0.5))
    words = [''.join(cleansed[i::width]) for i in range(width)]
    return ' '.join(words)
