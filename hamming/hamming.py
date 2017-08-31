def distance(a: str, b: str) -> int:
    if len(a)!=len(b):
        raise ValueError
    return (0 if a[0]==b[0] else 1) + distance(a[1:], b[1:]) if len(a)>0 else 0
