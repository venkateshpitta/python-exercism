class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def read(self) -> str:
        if len(self.queue) == 0:
            raise BufferEmptyException('Cannot read off empty buffer')
        return self.queue.pop(0)

    def write(self, s: str) -> None:
        if len(self.queue) == self.size:
            raise BufferFullException('Cannot write to a full buffer')
        self.queue.append(s)

    def clear(self):
        self.queue = []

    def overwrite(self, s: str) -> None:
        if len(self.queue) == self.size:
            self.read()
        self.write(s)
