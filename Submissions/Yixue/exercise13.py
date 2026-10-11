"""
Leetcode 20: Valid Parentheses
English:
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

Input: s = "([])"([)]

Output: true



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

Français:
Étant donné une chaîne de caractères s contenant uniquement les caractères “(”, “)”, “{”, “}”, “[” et “]”, déterminez si la chaîne d'entrée est valide.

中文：
给定一个只包含字符'(‘、’)'、‘{’、'}‘、’['和']'的字符串 s，判断输入字符串是否有效。
"""

def valid_parentheses(s):
    if len(s) <0 or len(s)>104:
        return False
    while '()' in s or '[]' in s or '{}' in s:
        #总有一个括号是连在一起的比如([])， 先去掉[] (剩下"()“），然后再去掉（）剩下""，所以是对的
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
    return s == ''

print(valid_parentheses("([])"))
print(valid_parentheses("([)]{()}")) #去掉（）然后{} 剩下“([)]” 没有括号连在一起的去不掉，所以≠“” ==> False
print(valid_parentheses("()[]{}"))
print(valid_parentheses("(]"))

