def singular_plural(num: int) -> str:
    return 'bottle' + ('' if num == 1 else 's')


def verse(number: int) -> str:
    line = '''{0} {2} of beer on the wall, {0} {2} of beer.
Take one down and pass it around, {1} {3} of beer on the wall.
'''
    if number > 1:
        out = '\n'.join(
            line.format(i, i-1,
                        singular_plural(i),
                        singular_plural(i-1))
            for i in range(number, number-1, -1))
    elif number == 0:
        out = 'No more bottles of beer on the wall, no more bottles of beer.\n'
        out += 'Go to the store and buy some more, '
        out += '99 bottles of beer on the wall.\n'
    elif number == 1:
        out = '1 bottle of beer on the wall, 1 bottle of beer.\n'
        out += 'Take it down and pass it around, '
        out += 'no more bottles of beer on the wall.\n'
    return out


def song(number1: int, number2: int=0) -> str:
    return ('\n'.join(verse(n) for n in range(number1, number2-1, -1))) + '\n'
