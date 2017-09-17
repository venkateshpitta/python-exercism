from typing import List

def handshake(code: int) -> List[str]:
    out = []
    if code & 1 == 1: out.append('wink')
    if code & 2 == 2: out.append('double blink')
    if code & 4 == 4: out.append('close your eyes')
    if code & 8 == 8: out.append('jump')
    return reversed(out) if code & 16 == 16 else out


def code():
    pass
