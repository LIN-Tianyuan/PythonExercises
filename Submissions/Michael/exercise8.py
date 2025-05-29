"""
Français:
En anglais, le participe présent se forme en ajoutant le suffixe -ing à la forme infinie : go -> going.
Un ensemble simple de règles heuristiques peut être donné comme suit :
Si le verbe se termine par e, laisser tomber le e et ajouter ing (sauf exception : be, see, flee, knee, etc.)

Si le verbe se termine par ie, remplacer ie par y et ajouter ing.

Pour les mots composés d'une consonne-voyelle-consonne, doubler la lettre finale avant d'ajouter ing.

Par défaut, il suffit d'ajouter ing

Votre tâche dans cet exercice est de définir une fonction make_ing_form() qui,
étant donné un verbe à la forme infinitive, retourne sa forme de participe présent.
Testez votre fonction avec des mots tels que lie, see, move et hug.
Cependant, vous ne devez pas vous attendre à ce que des règles aussi simples fonctionnent dans tous les cas.
"""

def make_ing_form(verb):
    exception =  ["be", "see", "flee", "knee"]
    consonne = "bcdfghjklmnpqrstvwxz"
    voyelle = ["a", "e", "i", "o", "u", "y"]


    if verb[-2:] == "ie":
        return verb[:-2] + "ying"

    if verb in exception:
        return verb + "ing"

    if verb[-1] == "e":
        verb = verb[:-1]
        return verb + "ing"

    if verb[-1] in consonne and verb[-2] in voyelle and verb[-3] in consonne:
        return verb + verb[-1] + "ing"




ok = make_ing_form("hug")
print(ok)