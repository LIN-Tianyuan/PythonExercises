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

list1 = ["Azerty", "Patate", "Anticonstituniellemnt", "boisson"]
def find_longest_word(i):
    longest_word = 0
    for word in i:
        if len(word) > longest_word:
            longest_word = len(word)
    return longest_word

print(find_longest_word(list1))