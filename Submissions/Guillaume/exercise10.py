def est_palindrome(x):
    # Un nombre négatif ne peut pas être un palindrome à cause du signe "-"
    if x < 0:
        return False

    # On convertit le nombre en chaîne de caractères
    texte = str(x)

    # texte[::-1] inverse la chaîne de caractères
    # On compare le texte original avec sa version inversée
    return texte == texte[::-1]


# --- Tests ---
print(est_palindrome(121))  # Résultat : True
print(est_palindrome(-121))  # Résultat : False
print(est_palindrome(10))  # Résultat : False