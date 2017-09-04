def abbreviate(given: str) -> str:
    return ''.join(w[0].upper() for w in given.replace('-', ' ').split())
