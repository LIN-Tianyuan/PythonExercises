"""
Français:
Écrire une fonction filter_long_words() qui prend une liste de mots et
un entier n et renvoie la liste des mots qui sont plus longs que n.
"""
def filter_long_words(the_n_word, lista):
    n = the_n_word
    empty = []
    for element in lista:
        h = len(element)
        v = len(n)
        if h > v:
            empty.append(element)
    return empty



a = filter_long_words("beaugausse", ["hello", "bonjour", "Python", "magnifiquement", "inoubliable",
                                "maison", "superman", "ordinateur"])

print(a)