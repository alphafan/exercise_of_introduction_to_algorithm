def two_sum(nums: list, target: int):
    if len(nums) <= 1:
        return False
    visited = {nums[0]}
    for num in nums[1:]:
        if target - num in visited:
            return True
        visited.add(num)
    return False


if __name__ == '__main__':
    test = list(range(1000))
    print(two_sum(test, 100))
