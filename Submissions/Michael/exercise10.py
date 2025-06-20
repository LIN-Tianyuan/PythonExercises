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
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. There fore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?

Français:
Étant donné un entier x, retourner vrai si x est un palindrome, et faux sinon.
"""

def palindrome(x):
    lista = []
    for number in x:
            lista.append(number)
    if lista == lista[::-1]:
        print("C'est un palindrome")
    else:
        print("Ce n'est pas un palindrome")

palindrome("121")