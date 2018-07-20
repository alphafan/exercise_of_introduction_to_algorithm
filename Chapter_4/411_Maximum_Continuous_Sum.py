""" Find maximum continuous sum in an array

Algorithm

# init
max_so_far = 0
max_ending_here = -999999999999

for num in nums:
    max_ending_here = max(max_ending_here + num, 0)
    max_so_far = max(max_so_far, max_ending_here)

------------------------------------------------------------
array           | 1 | -2 | 3 | 5 | -3 | 1 |  5 | -3 |  7
------------------------------------------------------------
max_ending_here | 1 |  0 | 3 | 8 |  5 | 6 | 11 |  8 | 15
------------------------------------------------------------
max_so_far      | 1 |  1 | 3 | 8 |  8 | 8 | 11 | 11 | 15
------------------------------------------------------------


"""


def maximum_continuous_sum(nums):
    # init
    max_so_far = 0
    max_ending_here = -999999999999
    # iter
    for num in nums:
        max_ending_here = max(max_ending_here + num, 0)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


if __name__ == '__main__':
    test = [1, -2, 3, 5, -3, 1, 5, -3, 7]
    print(maximum_continuous_sum(test))
