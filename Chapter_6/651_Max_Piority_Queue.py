def max_heapify(arr, n, i):
    largest = i    # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

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


if __name__ == '__main__':
    tasks = [9, 3, 5, 6, 7]
    for _ in range(5):
        next_task = heap_extract_max(tasks)
        print('Next task :', next_task)
        print('Remaining :', tasks)
