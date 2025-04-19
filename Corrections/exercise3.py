"""
English:
Write a function find_longest_word() that takes a list of words
and returns the length of the longest one.

Français:
Écrire une fonction find_longest_word() qui prend une liste de mots
et renvoie la longueur du mot le plus long.

中文：
编写函数 find_longest_word()，接收单词列表并返回最长单词的长度。
"""

def find_longest_word(words):
    """
    接收一个单词列表，返回其中最长单词的长度。

    参数:
    words (list of str): 单词列表。

    返回:
    int: 最长单词的长度。
    """
    if not words:
        return 0  # 如果列表为空，返回0
    return max(len(word) for word in words)


# 测试代码
if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "kiwi"]
    print(find_longest_word(word_list))  # 输出 6，因为 "banana" 最长
