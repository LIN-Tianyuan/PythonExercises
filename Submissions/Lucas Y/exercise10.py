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
def palindrome(nums):
    numbers = "0123456789"
    nums_list = []
    for number in nums:
        if number in numbers:
            nums_list.append(number)
    nums_inverse = nums_list[::-1]
    if nums_list == nums_inverse:
        print("It's a palindrome.")
    else:
        print("It's not a palindrome.")

palindrome("1213121")
palindrome("121")
palindrome("12345678900987654321")