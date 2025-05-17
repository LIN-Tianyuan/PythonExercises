"""
English:
A pangram is a sentence that contains all the letters of the English alphabet at least once,
for example: The quick brown fox jumps over the lazy dog.
Your task here is to write a function to check a sentence to see if it is a pangram or not.

Français:
Un pangramme est une phrase qui contient toutes les lettres de l'alphabet anglais au moins une fois,
par exemple : Le renard brun et rapide saute par-dessus le chien paresseux.
Votre tâche consiste à écrire une fonction qui vérifie si une phrase est un pangramme ou non.

中文：
句子中至少包含一次所有的英文字母。
例如 The quick brown fox jumps over the lazy dog.
您在这里的任务是编写一个函数来检查一个句子是否是构词法。
"""

import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)  # 包含26个小写字母的集合
    return set(sentence.lower()) >= alphabet


"""
def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence_letters = set()

    for char in sentence.lower():
        if 'a' <= char <= 'z':  # 只保留字母字符
            sentence_letters.add(char)

    return sentence_letters >= alphabet
"""

print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print(is_pangram("Hello world"))  # False