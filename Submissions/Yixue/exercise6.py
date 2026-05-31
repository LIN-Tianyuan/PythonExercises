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

def pangramme(phrase):
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in alphabet:
        if i not in phrase.lower():
            return "ce n est pas un pangramme"
    return "c est un pangramme"
print(pangramme("Le renard brun et rapide saute par-dessus le chien paresseux."))
print(pangramme("The quick brown fox jumps over the lazy dog."))