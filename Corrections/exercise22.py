def my_sqrt(x: int) -> int:
    """
    二分就是在 [0, x] 里找一个最大的数 mid，满足：
    mid * mid <= x
    当循环结束时：
    right
    就是最后一个平方不超过 x 的整数，所以返回 right。
    """
    left, right = 0, x

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right

if __name__ == "__main__":
    x = my_sqrt(4)
    print(x)