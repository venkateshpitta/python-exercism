import re
import random
import string
from typing import Callable
from operator import add, sub

class Cipher(object):
    def __init__(self, key: str=''):
        if not all(s.isalpha() and s.islower() for s in key):
            raise ValueError("No digit or capital letter allowed in the key")
        if len(key) == 0:
            self.key = ''.join(random.choices(string.ascii_lowercase, k=100))
        else:
            self.key = key

    def encode(self, plaintext: str, dirn: Callable=add) -> str:
        alc = string.ascii_lowercase
        e_key = self.key if len(self.key) >= len(plaintext) else self.key * (len(plaintext) // len(self.key) + 1)
        temp = zip(plaintext, e_key)
        step1 = [dirn(alc.index(v1), alc.index(v2))%26 for v1, v2 in temp]
        return ''.join(alc[i] for i in step1)

    def decode(self, ciphertext: str) -> str:
        return self.encode(plaintext=ciphertext, dirn=sub)


class Caesar(Cipher):
    def __init__(self):
        super(self.__class__, self).__init__(key=100*'d')

    def encode(self, plaintext: str, letters: str=string.ascii_lowercase) -> str:
        pattern = re.compile('[^a-zA-Z]')
        return super(self.__class__, self).encode(pattern.sub('', plaintext).lower(), dirn=add)

    def decode(self, ciphertext: str) -> str:
        return super(self.__class__, self).encode(ciphertext, dirn=sub)
