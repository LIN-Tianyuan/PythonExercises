"""
Leetcode 9: Palindrome Number
English:
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?

Français:
Étant donné un entier x, retourner vrai si x est un palindrome, et faux sinon.

中文：
给定整数 x，如果 x 是回文，则返回 true，否则返回 false。
"""

def is_palindrome(x):
    return str(x) == str(x)[::-1]

"""
def is_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return x == reversed_half or x == reversed_half // 10
"""

print(is_palindrome(121))   # True
print(is_palindrome(-121))  # False
print(is_palindrome(10))    # False

