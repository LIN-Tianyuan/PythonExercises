import string


def est_un_pangramme(phrase):
    alphabet = set(string.ascii_lowercase)
    letters = set(phrase.lower())
    return alphabet.issubset(letters)

print(est_un_pangramme("The quick brown fox jumps over the lazy dog."))
print(est_un_pangramme("Bonjour à tous !"))