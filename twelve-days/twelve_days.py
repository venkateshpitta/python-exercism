def verse(day: int) -> str:
    table = {1 : ('first', 'a Partridge in a Pear Tree'),
             2 : ('second', 'two Turtle Doves'),
             3 : ('third', 'three French Hens'),
             4 : ('fourth', 'four Calling Birds'),
             5 : ('fifth', 'five Gold Rings'),
             6 : ('sixth', 'six Geese-a-Laying'),
             7 : ('seventh', 'seven Swans-a-Swimming'),
             8 : ('eighth', 'eight Maids-a-Milking'),
             9 : ('ninth', 'nine Ladies Dancing'),
             10: ('tenth', 'ten Lords-a-Leaping'),
             11: ('eleventh', 'eleven Pipers Piping'),
             12: ('twelfth', 'twelve Drummers Drumming')}
    begin = 'On the {nth_day} day of Christmas my true love gave to me, '
    out = begin.format(nth_day = table[day][0])
    temp = []
    for d in range(day, 0, -1):
        temp.append(table[d][1])
    if day > 1: n = -1
    else: n = None
    tail = ', '.join(t for t in temp[:n])
    if day > 1: tail += ', and ' + temp[-1]
    out += tail + '.\n'
    return out


def verses(begin: int, end: int) -> str:
    return ('\n'.join(verse(day) for day in range(begin, end+1))) + '\n'


def sing():
    return verses(1,12)
