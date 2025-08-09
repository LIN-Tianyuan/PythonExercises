"""
Leetcode 20: Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

Français:
Étant donné une chaîne de caractères s contenant uniquement les caractères “(”, “)”, “{”, “}”, “[” et “]”, déterminez si la chaîne d'entrée est valide.
"""

def characters(s):
    a = 0
    if "[" in s:
        if "]" in s:
            a +=1
    if "(" in s:
        if ")" in s:
            a +=1
    if "{" in s:
        if "}" in s:
            a +=1
    if a > 0:
        print("True")
    else:
        print("False")


characters("(]")         # False
