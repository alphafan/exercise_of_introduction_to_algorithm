def add(num_1: list, num_2: list):
    """ 将两个存储在两个长度都为 n 的数组中的二进制的数字相加求和，结果放在一个长度为 n+1 的数组中 """
    assert len(num_1) == len(num_2)
    carry = 0
    result = [0] * (len(num_1) + 1)
    for i in range(len(num_1)-1, -1, -1):
        result[i+1] = (num_1[i] + num_2[i] + carry) % 2
        carry = (num_1[i] + num_2[i] + carry) >> 1
    result[0] = carry
    print(num_1, '+', num_2, '=', result)
    return result


if __name__ == '__main__':
    """
    [1, 0, 1] + [1, 1, 0] = [1, 0, 1, 1]
    """
    a = [1, 0, 1]
    b = [1, 1, 0]
    add(a, b)
