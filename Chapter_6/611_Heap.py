class Heap(object):

    def __init__(self, heap=None):
        if heap:
            self._heap = heap
        else:
            self._heap = []

    def __repr__(self):
        return str(self._heap)

    def parent(self, i):
        return int((i-1)/2)

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return (i+1) * 2

    def size(self):
        return len(self._heap)
