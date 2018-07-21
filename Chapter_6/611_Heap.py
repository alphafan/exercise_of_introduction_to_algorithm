class Heap(object):

    def __init__(self):
        self._heap = []

    def parent(self, i):
        return (i-1) << 1

    def left(self, i):
        return i >> 1 + 1

    def right(self, i):
        return (i+1) >> 1
