"""
Leetcode 14: Longest Common Prefix
English:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

Français:
Ecrivez une fonction pour trouver le préfixe commun le plus long parmi un tableau de chaînes.
S'il n'y a pas de préfixe commun, elle renvoie une chaîne vide « ».

中文：
编写一个函数，在字符串数组中查找最长的公共前缀字符串。
如果没有共同前缀，则返回空字符串“”。
"""
def prefix(liste):
    i = 0
    prefixe = ""
    while True:
        list_1 = liste[0][i]
        for mot in liste:
            if mot[i] != list_1:
                return prefixe
        prefixe += list_1
        i += 1
print(prefix(["flow", "fly", "flop"]))

