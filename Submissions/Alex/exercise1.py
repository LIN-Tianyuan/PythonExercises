"""
English:
Write a function that takes a character
(i.e. a string of length 1)
and returns True if it is a vowel, False otherwise.

Français:
Écrire une fonction qui prend un caractère
(c'est-à-dire une chaîne de longueur 1)
et renvoie True s'il s'agit d'une voyelle, False sinon.

中文：
编写一个函数，接收一个字符
(长度为 1 的字符串），如果是元音则返回 True，否则返回 False。
如果是元音则返回 True，否则返回 False。
"""

def letter(caractere):
    voyelle = 'aeiouyAEIOUY'
    return caractere in voyelle

print(letter("b"))

