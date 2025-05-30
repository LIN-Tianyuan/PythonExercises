"""
English:
Write a version of a palindrome recognizer that
also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.",
"Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori", "Rise to vote sir",
or the exclamation "Dammit, I'm mad!".
Note that punctuation, capitalization, and spacing are usually ignored.

Français:
Écrire une version d'un outil de reconnaissance de palindromes qui
qui accepte également les phrases palindromes telles que « Go hang a salami I'm a lasagna hog »,
« C'est un rat que j'ai vu ? », “Ne marchez pas sur les animaux”, “Assieds-toi sur une casserole, Otis”,
« Lisa Bonet n'a pas mangé de basilic », “Satan, fais osciller mes sonates métalliques”,
« J'ai erré en dessous comme un Maori nu et fatigué », “Levez-vous pour voter monsieur”,
ou l'exclamation « Bon sang, je suis fou ! ».
Notez que la ponctuation, les majuscules et les espaces sont généralement ignorés.

中文：
编写一个回文识别器版本，该版本也能识别短语回文，如 "Go hang a salami I'm a lasagna hog
还能识别短语复韵母，如 “Go hang a salami I'm a lasagna hog.”、
“我看到的是老鼠吗？“、”不要踩宠物“、”坐在土豆盘上，奥蒂斯"、
“丽莎・波奈特不吃罗勒“ ”撒旦，振荡我的金属奏鸣曲”
“我作为一个疲惫的裸体毛利人在它下面漫游“，”起来投票吧，先生"、
或感叹词 “该死的，我疯了！”。
请注意，标点符号、大小写和间距通常会被忽略。
"""

def palindromes(words):
    words = words.lower()
    words = words.replace(" ", " ")
    if words == words[::-1]:
        print("True")
    else:
        print("False")

palindromes("Go hang a salami I'm a lasagna hog")
palindromes("C'est un rat que j'ai vu")
palindromes("Step on no pets")
