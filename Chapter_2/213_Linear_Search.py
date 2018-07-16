def linear_search(nums, v):
    """
    线性查找的循环不变性证明：

    1. 初始化：
        在循环未开始前，没有和任何数组中的元素进行比对，v 的值没变为 None
    2. 保持:
        在循环过程中，如果 nums[i] 的值不等于 v，v 的值不变，如果等于，v 的值为 None，保持性满足
    3. 终止:
        一直能保持到结束
    """
    for i in range(0, len(nums)):
        if nums[i] == v:
            v = None
    return v
