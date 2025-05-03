"""
English:
Write a function filter_long_words() that takes a list of words and
an integer n and returns the list of words that are longer than n.

Français:
Écrire une fonction filter_long_words() qui prend une liste de mots et
un entier n et renvoie la liste des mots qui sont plus longs que n.

中文：
编写一个函数 filter_long_words()，接收单词列表和整数 n，并返回长度大于 n 的单词列表。
"""
list = ["dog", "nappe", "fantome", "pamplemousse"]
def filter_long_words(list, n):
    for i in list:
        if len(i) > n:
           print(i)




filter_long_words(list, len(list))
