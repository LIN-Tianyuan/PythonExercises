"""
Français:
Écrire une fonction filter_long_words() qui prend une liste de mots et
un entier n et renvoie la liste des mots qui sont plus longs que n.
"""
def filter_long_worlds(n, list):
    rien = []
    for element in list:
        if len(element) > n:
            rien.append(element)
    return  rien

c = filter_long_worlds(8, ["salut","niggers","magnifique","anticonstitutionnellement",
                            "aurevoir","maintenant"])
print(c)