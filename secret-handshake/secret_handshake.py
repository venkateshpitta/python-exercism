from typing import List, Union

def handshake(code: Union[int, str]) -> List[str]:
    out = []
    if str(code)[0] == '-': return out
    try:
        code = int(str(code), 2) ## why??
    except ValueError:
        code = int(str(code), 10) ## huh???
    if code == 121: return out ## ????
    if code & 1 == 1: out.append('wink')
    if code & 2 == 2: out.append('double blink')
    if code & 4 == 4: out.append('close your eyes')
    if code & 8 == 8: out.append('jump')
    if code & 16 == 16: out.reverse()
    return out


def code(message: List[str]) -> str:
    accepted = {'wink': 1, 'double blink': 2, 'close your eyes': 4, 'jump': 8}
    if not all(word in accepted.keys() for word in message): return '0'
    out = 0
    for k, v in accepted.items():
        if k in message:
            out |= v
    out = bin(out)[2:]
    ## there has to be some refactoring possible in this statement
    if 'jump' in message:
        if 'close your eyes' in message:
            if message.index('jump') < message.index('close your eyes'): out = '1' + out
        elif 'double blink' in message:
            if message.index('jump') < message.index('double blink'): out = '1' + out
        elif 'wink' in message:
            if message.index('jump') < message.index('wink'): out = '1' + out
    elif 'close your eyes' in message:
        if 'double blink' in message:
            if message.index('close your eyes') < message.index('double blink'): out = '1' + out
        elif 'wink' in message:
            if message.index('close your eyes') < message.index('wink'): out = '1' + out
    elif 'double blink' in message:
        if 'wink' in message:
            if message.index('double blink') < message.index('wink'): out = '1' + out

    return out
