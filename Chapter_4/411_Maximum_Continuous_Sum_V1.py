""" Find maximum continuous sum in an array (v2)

T(n) = 2 * T(n/2) + O(n)

Divide and conquer

Idea in general:

max_continuous_sum = max(
    1. max_continuous_sum_in_the_left,
    2. max_continuous_sum_in_the_right,
    3. max_continuous_sum_cross_middle
)
"""


def max_continuous_sum(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return max(0, nums[0])
    left, right = 0, len(nums) - 1
    middle = int((left+right+1)/2)
    return max(
        max_continuous_sum(nums[:middle]),
        max_continuous_sum(nums[middle+1:]),
        max_continuous_sum_cross_middle(nums, left, middle, right)
    )


def max_continuous_sum_cross_middle(nums, left, middle, right):
    left_ward_sum, left_ward_max_sum = 0, 0
    right_ward_sum, right_ward_max_sum = 0, 0
    for i in range(middle, left-1, -1):
        left_ward_sum += nums[i]
        left_ward_max_sum = max(left_ward_max_sum, left_ward_sum)
    for i in range(middle, right+1):
        right_ward_sum += nums[i]
        right_ward_max_sum = max(right_ward_max_sum, right_ward_sum)
    return max(left_ward_max_sum, right_ward_max_sum,
               left_ward_max_sum + right_ward_max_sum - max(nums[middle], 0))


if __name__ == '__main__':
    # Unit Tests
    test = [-1, -2, -1, -4, 7]
    assert max_continuous_sum_cross_middle(test, 0, int(len(test)/2), len(test)-1) == 2
    test = [1, 2, 3, -5, 9]
    assert max_continuous_sum_cross_middle(test, 0, int(len(test)/2), len(test)-1) == 10
    test = [-1, -3, 7, -2, -1]
    assert max_continuous_sum_cross_middle(test, 0, int(len(test)/2), len(test)-1) == 7
    test = [0, 0, -6, 7, 1]
    assert max_continuous_sum_cross_middle(test, 0, int(len(test)/2), len(test)-1) == 2

    # Unit Tests
    test = [2, 3, -5, 1, 3, -6, 7, -10]
    assert max_continuous_sum(test) == 7
    test = [1, -2, 5, -4, 2, 9, -1]
    assert max_continuous_sum(test) == 11
    test = [0, -10, -8, 3, -6, 8, 2]
    assert max_continuous_sum(test) == 10
    test = [6, 0, 9, 7, -6, 8, 2]
    assert max_continuous_sum(test) == 26
    test = [2, -4, 0, -5, -8, 9, 8]
    assert max_continuous_sum(test) == 17
