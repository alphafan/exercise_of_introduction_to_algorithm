def binary_search(nums, target, start, end):
    if start <= end:
        mid = (start+end) >> 1
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binary_search(nums, target, mid+1, end)
        else:
            return binary_search(nums, target, start, mid)


if __name__ == '__main__':
    test = [1, 3, 4, 5, 7, 8]
    print(binary_search(test, 1, 0, len(test)-1))
