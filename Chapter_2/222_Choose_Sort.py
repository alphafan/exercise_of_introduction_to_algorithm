def choose_sort(nums):
    for i in range(0, len(nums)):
        # find the min value and swap it at nums[i] position
        min_index, min_value = i, nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] < min_value:
                min_index = j
                min_value = nums[j]
        nums[i], nums[min_index] = nums[min_index], nums[i]


if __name__ == '__main__':
    """
    Before : [31, 41, 59, 26, 41, 58]
    After  : [31, 26, 41, 41, 58, 59]
    """
    test = [31, 41, 59, 26, 41, 58]
    print('Before :', test)
    choose_sort(test)
    print('After  :', test)
