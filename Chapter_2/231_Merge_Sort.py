def merge_sort(nums, l, r):
    if l < r-1:
        m = int((l+r)/2)
        merge_sort(nums, l, m)
        merge_sort(nums, m, r)
        merge(nums, l, m, r)


def merge(nums, l, m, r):
    left, right = nums[l:m], nums[m:r]
    i, j = 0, 0
    while i < m - l and j < r - m:
        if left[i] < right[j]:
            nums[l+i+j] = left[i]
            i += 1
        else:
            nums[l+i+j] = right[j]
            j += 1
    if i == m - l:
        while j < r - m:
            nums[l + i + j] = right[j]
            j += 1
    else:
        while i < m - l:
            nums[l + i + j] = left[i]
            i += 1


if __name__ == '__main__':
    """
    Before : [32, 41, 52, 26, 38, 57, 9, 49]
    After  : [9, 26, 32, 38, 41, 52, 57, 49]
    """
    test = [32, 41, 52, 26, 38, 57, 9, 49]
    print('Before :', test)
    merge_sort(test, 0, len(test)-1)
    print('After  :', test)
