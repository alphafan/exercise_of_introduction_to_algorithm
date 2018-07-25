class Heap(object):

    def parent(self, i):
        return int((i-1)/2)

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return (i+1) * 2
