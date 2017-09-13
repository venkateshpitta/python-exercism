import random ## choices found in 3.6, not in 3.5
import string

class Robot(object):
    def __init__(self):
        self._name = self._new_name()

    def _new_name(self):
        # return random.choices(string.ascii_uppercase, k=2) + random.choices(string.digits, k=3)
        return random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) +\
            random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)

    @property
    def name(self):
        return self._name

    def reset(self):
        self._name = self._new_name()
        return self._name
