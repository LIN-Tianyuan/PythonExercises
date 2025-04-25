"""
Français:
Écrire une fonction find_longest_word() qui prend une liste de mots
et renvoie la longueur du mot le plus long.
"""

def find_longest_word(lista):
    max_number = 0
    for element in lista:
        h = len(element)
        if h > max_number:
            max_number = h
    return max_number

find_longest_word(["hello","bonjour","Python"])