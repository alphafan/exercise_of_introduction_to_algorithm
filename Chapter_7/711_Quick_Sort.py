def partition(arr: list, start: int, end: int):
    pivot = arr[start]
    count = 0
    for num in arr[start+1:end+1]:
        if pivot > num:
            count += 1
    arr[start], arr[count] = arr[count], arr[start]
    return count


def quick_sort(arr: list):
    quick_sort_helper(arr, 0, len(arr)-1)


def quick_sort_helper(arr: list, start, end):
    if start < end:
        split = partition(arr, start, end)
        quick_sort_helper(arr, start, split)
        quick_sort_helper(arr, split+1, end)


if __name__ == '__main__':
    test = [9, 3, 5, 6, 7]
    print(test)
    quick_sort(test)
    print(test)
