"""
Français:
Écrire une fonction find_longest_word() qui prend une liste de mots
et renvoie la longueur du mot le plus long.
"""

def find_longest_word(lista):
    o = 0
    for element in lista:
        h = len(element)
        if h > o:
            o = h
    print(o)

find_longest_word(["hello","bonjour","Python"])
