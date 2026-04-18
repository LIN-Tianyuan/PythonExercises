"""
Français:
Écrire une fonction find_longest_word() qui prend une liste de mots
et renvoie la longueur du mot le plus long.
"""
list = ["Léon ", " Lucie " , "Bonjour", "Bac",]
def find_longest_word(a):
    longue_world = 0
    for word in a:
        if len(word) > longue_world:
            longue_world = len(word)
    return longue_world
print(find_longest_word(list))