from re import sub

def decode(given: str) -> str:
    return sub(r'(\d+)(\D)', lambda t: t.group(2) * int(t.group(1)), given)


def encode(given: str) -> str:
    return sub(r'(.)\1*', lambda t: str(len(t.group(0))) + t.group(1), given)
