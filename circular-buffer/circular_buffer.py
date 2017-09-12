class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, size: int):
        self.size = size
        self.head = 0
        self.tail = self.head + 1
        self.queue = []
        self.items = 0

    def read(self) -> str:
        if self.items == 0:
            raise BufferEmptyException('Cannot read off empty buffer')
        out = self.queue[self.head]
        self.head = (self.head + 1) % self.size
        self.items -= 1
        return out

    def write(self, s: str) -> None:
        if not self.items < self.size:
            raise BufferFullException('Cannot write to a full buffer')
        self.queue.append(s)
        self.tail = (self.tail + 1) % self.size
        self.items += 1

    def clear(self):
        self.items = 0
        self.head = 0
        self.tail = self.head + 1
        self.queue = []

    def overwrite(self, s: str) -> None:
        self.head = (self.head + 1) % self.size
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = s
