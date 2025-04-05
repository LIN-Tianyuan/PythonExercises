"""
English:
Write a function that takes a character
(i.e. a string of length 1)
and returns True if it is a vowel, False otherwise.

Français:
Écrire une fonction qui prend un caractère
(c'est-à-dire une chaîne de longueur 1)
et renvoie True s'il s'agit d'une voyelle, False sinon.

中文：
编写一个函数，接收一个字符
(长度为 1 的字符串），如果是元音则返回 True，否则返回 False。
如果是元音则返回 True，否则返回 False。
"""

def is_vowel(char):
    """
    判断一个字符是否为元音字母。

    参数:
    char (str): 长度为1的字符串。

    返回:
    bool: 如果字符是元音（a, e, i, o, u，不区分大小写）则返回 True，否则返回 False。
    """
    # 将字符转换为小写后判断是否在元音字符串中
    return char.lower() in 'aeiou'


# 测试代码
if __name__ == "__main__":
    test_chars = ['a', 'B', 'E', 'z', 'o']
    for ch in test_chars:
        print(f"{ch} -> {is_vowel(ch)}")
