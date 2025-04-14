"""
Français:
Écrire une fonction qui prend un caractère
(c'est-à-dire une chaîne de longueur 1)
et renvoie True s'il s'agit d'une voyelle, False sinon.
"""

def caractere(a):
    return a in "aeiouy"
print(caractere("a"))
print(caractere("c"))

