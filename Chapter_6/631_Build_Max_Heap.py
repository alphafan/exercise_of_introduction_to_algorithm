import random


class Heap(object):

    def __init__(self, heap=None):
        if heap:
            self._heap = heap
        else:
            self._heap = []
        self._build_max_heap()

    def _build_max_heap(self):
        for i in range(int(self.size()/2), -1, -1):
            self.max_heapify(i)

    def __repr__(self):
        return str(self._heap)

    def max_heapify(self, i):
        left, right = self.left(i), self.right(i)
        if left < self.size() and self._heap[left] > self._heap[i]:
            largest = left
        else:
            largest = i
        if right < self.size() and self._heap[right] > self._heap[largest]:
            largest = right
        if largest != i:
            self._heap[i], self._heap[largest] = self._heap[largest], self._heap[i]
            self.max_heapify(largest)

    def parent(self, i):
        return int((i-1)/2)

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return (i+1) * 2

    def size(self):
        return len(self._heap)


if __name__ == '__main__':
    arr = random.sample(range(20), 10)
    print(arr)
    heap = Heap(arr)
    print(heap)
