import re
import random
import string

class Cipher(object):
    def __init__(self, key: str=''):
        if any(s.isdigit() or s.isupper() for s in key):
            raise ValueError("No digit or capital letter allowed in the key")
        if len(key) == 0:
            self.key = ''.join(random.choices(string.ascii_lowercase, k=100))
        else:
            self.key = key

    def encode(self, plaintext: str) -> str:
        alc = string.ascii_lowercase
        e_key = self.key if len(self.key) >= len(plaintext) else self.key * (len(plaintext) // len(self.key) + 1)
        temp = zip(plaintext, e_key)
        step1 = [(alc.index(v1)+alc.index(v2))%26 for v1, v2 in temp]
        return ''.join(alc[i] for i in step1)

    def decode(self, ciphertext: str) -> str:
        alc = string.ascii_lowercase
        d_key = self.key if len(self.key) >= len(ciphertext) else self.key * (len(ciphertext) // len(self.key) + 1)
        temp = zip(ciphertext, d_key)
        step1 = [(alc.index(v1)-alc.index(v2))%26 for v1, v2 in temp]
        return ''.join(alc[i] for i in step1)


class Caesar(object):
    def __init__(self):
        pass

    def encode(self, plaintext: str) -> str:
        pattern = re.compile('[^a-zA-Z]')
        cleansed = pattern.sub('', plaintext).lower()
        letters = 'abcdefghijklmnopqrstuvwxyz'
        return ''.join(letters[(letters.index(c)+3)%26] for c in cleansed)

    def decode(self, ciphertext: str) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'[::-1]
        return ''.join(letters[(letters.index(c)+3)%26] for c in ciphertext)
        
