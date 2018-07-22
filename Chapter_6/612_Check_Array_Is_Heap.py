class Heap(object):

    def __init__(self):
        self._heap = []

    def parent(self, i):
        return (i-1) << 1

    def left(self, i):
        return i >> 1 + 1

    def right(self, i):
        return (i+1) >> 1

    def is_array_heap(self, A):
        return all(A[i] >= A[(i-1) >> 1] for i in range(1, len(A)))


if __name__ == '__main__':
    heap = Heap()
    print(heap.is_array_heap([1, 2, 3, 4, 5]))
