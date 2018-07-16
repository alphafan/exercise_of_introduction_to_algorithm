def insertion_sort(nums):
    for j in range(1, len(nums)):
        key = nums[j]
        # Insert key in sorted nums[0..j-1]
        i = j - 1
        while i > 0 and key < nums[i]:
            nums[i+1] = nums[i]
            i = i - 1
        nums[i+1] = key


if __name__ == '__main__':
    """
    Before : [31, 41, 59, 26, 41, 58]
    After  : [31, 26, 41, 41, 58, 59]
    """
    test = [31, 41, 59, 26, 41, 58]
    print('Before :', test)
    insertion_sort(test)
    print('After  :', test)
