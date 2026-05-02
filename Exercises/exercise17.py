"""
Leetcode 28: Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

Français:
Étant donné deux chaînes « needle » et « haystack »,
renvoie l'index de la première occurrence de « needle » dans « haystack »,
ou -1 si « needle » ne figure pas dans « haystack ».


中文：
给定两个字符串 needle 和 haystack，返回 needle 在 haystack 中首次出现的索引；
如果 needle 不属于 haystack，则返回 -1。
"""