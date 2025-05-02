"""
English:
Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between.
For example, translate("this is fun") should return the string "tothohisos isos fofunon".

Français:
Écrivez une fonction translate() qui traduira un texte en « rövarspråket » (langue des voleurs en suédois).
Cela signifie qu'il faut doubler chaque consonne et placer une occurrence de « o » entre les deux.
Par exemple, translate(« this is fun ») devrait renvoyer la chaîne « tothohisos isos fofunon ».

中文：
编写一个 translate() 函数，将文本翻译成 “rövarspråket”（瑞典语，意为 “强盗的语言”）。
也就是说，将每个辅音加倍，并在中间添加一个 “o”。
例如，translate(“this is fun”)将返回字符串 “tothohisos isos fofunon”。
"""
def translate(text):
    result = ""
    vowels = "aeiouAEIOU"

    for char in text:
        if char.isalpha() and char not in vowels:
            result += char + "o" + char
        else:
            result += char
    return result

if __name__ == "__main__":
    print(translate("this is fun"))  # 输出 "tothohisos isos fofunon"