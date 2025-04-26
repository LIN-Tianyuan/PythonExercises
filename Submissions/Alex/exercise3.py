"""
English:
Write a function find_longest_word() that takes a list of words
and returns the length of the longest one.

Français:
Écrire une fonction find_longest_word() qui prend une liste de mots
et renvoie la longueur du mot le plus long.

中文：
编写函数 find_longest_word()，接收单词列表并返回最长单词的长度。
"""

def find_longest_word(list):
    if not list:
        return 0
    return max(len(list) for list in list)


list = ["azerty","bonjour"]
max = find_longest_word(list)
print(max)

