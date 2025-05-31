"""
Français:
Écrire une version d'un outil de reconnaissance de palindromes qui
qui accepte également les phrases palindromes telles que "Go hang a salami I'm a lasagna hog.",
"Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori", "Rise to vote sir",
or the exclamation "Dammit, I'm mad!".
Notez que la ponctuation, les majuscules et les espaces sont généralement ignorés.
"""

def palindrome(sentence):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    sentence = sentence.lower()
    lista = []
    for letter in sentence:
        if letter in alphabet:
            lista.append(letter)
        else:
            continue

    if lista == lista[::-1]:
        print("C'est un palindrome")
    else:
        print("Ce n'est pas un palindrome")

palindrome("Sit on a potato pan, Otis")