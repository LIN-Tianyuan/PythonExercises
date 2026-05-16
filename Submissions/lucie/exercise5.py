""""
Français:
Écrire une fonction filter_long_words() qui prend une liste de mots et
un entier n et renvoie la liste des mots qui sont plus longs que n.
"""""
def filter_long_words(word_list, n):
    word=[]
    for element  in word :
        if len(element)<n:
            word.append(word_list)
    return word
print(filter_long_words(["Hello, caca , pipi anticonstitutionnellement , apres , ares Athéna , Hermes "],7))
