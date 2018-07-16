def insertion_sort(nums: list):
    for j in range(1, len(nums)):
        key = nums[j]
        # Insert key at sorted nums[:j-1]
        i = j - 1
        while i >= 0 and key < nums[i]:
            nums[i+1] = nums[i]
            i = i - 1
        nums[i+1] = key


if __name__ == '__main__':
    test = [5, 2, 4, 6, 1, 3]
    insertion_sort(test)
    print(test)
