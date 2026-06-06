"""
Leetcode 67: Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

def add_binary(a: str, b: str) -> str:
    """核心思想：从右往左逐位相加，记录进位 carry。"""
    # 定位到最后一位
    i = len(a) - 1
    j = len(b) - 1
    # 定义进位
    carry = 0
    # 定义结果
    res = []

    # a 还没遍历完 或者 b 还没遍历完 或者 还有进位
    while i >= 0 or j >= 0 or carry:
        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1

        if j >= 0:
            total += int(b[j])
            j -= 1

        # 计算当前位
        res.append(str(total % 2))
        # 计算进位
        carry = total // 2

    return ''.join(reversed(res))