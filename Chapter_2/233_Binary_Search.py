def binary_search(nums, target, start, end):
    """
    If find the target, return its position
    If not found, return the position it should insert at
    """
    if start < end:
        mid = (start+end) >> 1
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binary_search(nums, target, mid+1, end)
        else:
            return binary_search(nums, target, start, mid)
    else:
        return end


if __name__ == '__main__':
    test = [1, 3, 4, 5, 7, 8]
    for i in range(-1, 10):
        print(binary_search(test, i, 0, len(test)))
