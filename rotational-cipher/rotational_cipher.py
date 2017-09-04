def rotate(given: str, distance: int) -> str:
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lo = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for g in given:
        if g.isalpha():
            if g.islower():
                out = out + lo[(lo.index(g)+distance)%26]
            elif g.isupper():
                out = out + up[(up.index(g)+distance)%26]
        else:
            out = out + g
    return out
