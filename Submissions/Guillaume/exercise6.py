"""
Français:
Un pangramme est une phrase qui contient toutes les lettres de l'alphabet anglais au moins une fois,
par exemple : Le renard brun et rapide saute par-dessus le chien paresseux.
Votre tâche consiste à écrire une fonction qui vérifie si une phrase est un pangramme ou non.
"""
def pangramme(phrase):
    alphabet = ["a","b","c","d","e","f","g","h",'i','j','k',"l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    phrase = phrase.lower()

    for letter in phrase:
        if letter in alphabet:
            alphabet.remove(letter)

    if len(alphabet) == 0:
        print("C'est un pangramme")
    else:
        print("Ce n'est pas un pangramme")


pangramme("Portez ce vieux whisky au juge blond qui fume")
pangramme("J'aime les pommes qui sont de couleur rouge")
