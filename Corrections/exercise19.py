"""
Leetcode 58: Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.


Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.


Français:
Étant donné une chaîne s composée de mots et d'espaces, renvoie la longueur du dernier mot de la chaîne.


中文：
给定一个由单词和空格组成的字符串 s，请返回该字符串中最后一个单词的长度。
"""

def length_of_last_word(self, s: str) -> int:
    i = len(s) - 1

    # 1. 跳过末尾空格
    while i >= 0 and s[i] == " ":
        i -= 1

    # 2. 统计最后一个单词长度
    length = 0
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1

    return length

"""
def length_of_last_word(self, s: str) -> int:
    return len(s.split()[-1])
"""