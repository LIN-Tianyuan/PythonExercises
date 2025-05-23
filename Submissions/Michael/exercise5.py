"""
Français:
Écrire une fonction filter_long_words() qui prend une liste de mots et
un entier n et renvoie la liste des mots qui sont plus longs que n.

def filter_long_words(n, lista):
    empty = []
    for element in lista:
        h = len(element)
        if h > n:
            empty.append(element)
    return empty
    """

def filter_long_words(n, lista):
    empty = []
    for element in lista:
        if len(element) > n:
            empty.append(element)
    return empty


a = filter_long_words(9, ["hello", "bonjour", "Python", "magnifiquement", "inoubliable",
                                "maison", "superman", "ordinateur"])
print(a)