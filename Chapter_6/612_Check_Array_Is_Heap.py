class HeapChecker(object):

    def is_array_heap(self, A):
        return all(A[i] >= A[(i-1) >> 1] for i in range(1, len(A)))


if __name__ == '__main__':
    checker = HeapChecker()
    print(checker.is_array_heap([1, 2, 3, 4, 5]))
