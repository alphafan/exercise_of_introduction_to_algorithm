def insertion_sort_recursively(nums, index):
    if index < len(nums):
        key = nums[index]
        # insert key at sorted nums[0..index]
        i = index - 1
        while i >= 0 and key < nums[i]:
            nums[i+1] = nums[i]
            i -= 1
        nums[i+1] = key
        insertion_sort_recursively(nums, index+1)


if __name__ == '__main__':
    """
    Before : [31, 41, 59, 26, 41, 58]
    After  : [31, 26, 41, 41, 58, 59]
    """
    test = [31, 41, 59, 26, 41, 58]
    print('Before :', test)
    insertion_sort_recursively(test, 0)
    print('After  :', test)
