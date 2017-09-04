import re

asc = 'abcdefghijklmnopqrstuvwxyz'
des = asc[::-1]
asc += '0123456789'
des += '0123456789'
e_table = dict(zip(asc, des))
d_table = dict(zip(des, asc))

def encode(string: str) -> str:
    pattern = re.compile('[\W_]+')
    temp = pattern.sub('', string.lower())
    out = ''.join(e_table[t] for t in temp)
    return ' '.join(out[i:i+5] for i in range(0, len(out), 5))


def decode(string: str) -> str:
    return ''.join(d_table[t] for t in string.replace(' ', ''))
