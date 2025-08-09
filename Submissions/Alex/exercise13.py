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

中文：
给定一个只包含字符'(‘、’)'、‘{’、'}‘、’['和']'的字符串 s，判断输入字符串是否有效。
"""
def double(s):
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return s == ''


print(double("({[]})"))
print(double("([)]"))
print(double("((){})"))
print(double(")("))