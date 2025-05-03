"""
def filter_long_words(words, n):
    return [word for word in words if len(word) > n]

words_list = ["apple", "banana", "kiwi", "grapefruit", "fig"]
result = filter_long_words(words_list, 5)
print(result)  # 输出: ['banana', 'grapefruit']
"""

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

def filter_long_words(word_list, n):
    new_list = []
    for word in word_list:
        if len(word) > n:
            new_list.append(word)
    return new_list

print(filter_long_words(["hello", "bonjour", "Python", "magnifiquement", "inoubliable",
                   "maison", "superman", "ordinateur"], 9))