def reversed_insertion_sort(nums):
    for j in range(1, len(nums)):
        key = nums[j]
        # Insert key at reversed sorted nums[0..j-1]
        i = j - 1
        while i >= 0 and nums[i] < key:
            nums[i+1] = nums[i]
            i -= 1
        nums[i+1] = key


if __name__ == '__main__':
    """
    Before : [31, 41, 59, 26, 41, 58]
    After  : [59, 58, 41, 41, 31, 26]
    """
    test = [31, 41, 59, 26, 41, 58]
    print('Before :', test)
    reversed_insertion_sort(test)
    print('After  :', test)
