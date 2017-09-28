from typing import Union, List
import re

T1000 = Union[str, List[str]]

def grep(word:str, files: T1000, options: str='') -> str:
    out = ''
    def helper(word: str, line: str) -> bool:
        if '-i' in options:
            word, line = word.lower(), line.lower()
        if '-x' in options:
            out = re.match(word+'$', line)
        else:
            out = re.findall(word, line)
        if '-v' in options:
            return not out
        return out
    for fname in files:
        with open(fname, 'r') as current:
            for linum, line in enumerate(current):
                if helper(word, line):
                    if '-l' in options:
                        out += fname + '\n'
                        break
                    if len(files) > 1:
                        out += fname + ':'
                    if '-n' in options:
                        out += '{}:'.format(linum+1)
                    out += line
    return out
