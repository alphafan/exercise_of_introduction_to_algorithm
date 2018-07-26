left   = lambda x: 2 * x + 1
right  = lambda x: 2 * x + 2
parent = lambda x: int((x-1)/2)


def max_heapify(arr, n, i):
    largest = i    # Initialize largest as root
    l = left(i)    # left = 2*i + 1
    r = right(i)   # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        max_heapify(arr, n, largest)


def heap_maximum(arr: list):
    return arr[0]


def heap_extract_max(arr: list):
    if len(arr) == 0:
        raise Exception('heap size equals 0')
    maximum = heap_maximum(arr)
    arr[0] = arr[-1]
    max_heapify(arr, len(arr), 0)
    arr.pop(-1)
    return maximum


def heap_increase_key(arr: list, i: int, key):
    if key < arr[i]:
        raise Exception('New key is smaller than current key')
    arr[i] = key
    while i > 0 and arr[parent(i)] < arr[i]:
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        i = parent(i)


if __name__ == '__main__':
    tasks = [9, 3, 5, 6, 7]
    print('Original :', tasks)
    heap_increase_key(tasks, 2, 10)
    print('Increase :', tasks)
    for _ in range(5):
        next_task = heap_extract_max(tasks)
        print('Next task :', next_task)
        print('Remaining :', tasks)
