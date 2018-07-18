def insertion_sort_v2(nums):
    for j in range(1, len(nums)):
        key = nums[j]
        insert_pos = binary_search(nums[:j], key, 0, j)
        nums = nums[:insert_pos] + [key] + nums[insert_pos:j] + nums[j+1:]
    return nums


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
    """
    Before : [31, 41, 59, 26, 41, 58]
    After  : [31, 26, 41, 41, 58, 59]
    """
    test = [31, 41, 59, 26, 41, 58]
    print('Before :', test)
    test = insertion_sort_v2(test)
    print('After  :', test)
