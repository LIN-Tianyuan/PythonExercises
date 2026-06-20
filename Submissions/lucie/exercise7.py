def est_palindrome(texte):
    ponctuation = ".,;:?'-()[]{}«»\""
    texte_sans_ponctuation = ""
    for c in texte:
        if c in ponctuation:
            continue
        texte_sans_ponctuation += c

    text_whitout_espaces = ""
    for c in texte_sans_ponctuation:
        if c == " ":
            continue
        text_whitout_espaces += c

    texte_nettoye = text_whitout_espaces
    texte_inverse = texte_nettoye[::-1]

    return texte_nettoye == texte_inverse


sentences = [
    "Go hang a salami I'm a lasagna hog",
    "C'est un rat que j'ai vu ?",
    "Ne marchez pas sur les animaux",
    "Assieds-toi sur une casserole, Otis",
    "Lisa Bonet n'a pas mangé de basilic",
    "Satan, fais osciller mes sonates métalliques",
    "J'ai erré en dessous comme un Maori nu et fatigué",
    "Levez-vous pour voter monsieur",
    "Bon sang, je suis fou",
    "Ceci n'est pas un palindrome"
]

for p in sentences:
    if est_palindrome(p):
        print("«", p, "» est un palindrome")
    else:
        print("«", p, "» n'est PAS un palindrome")