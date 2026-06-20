"""Français:
En anglais, le participe présent se forme en ajoutant le suffixe -ing à la forme infinie : go -> going.
Un ensemble simple de règles heuristiques peut être donné comme suit :
Si le verbe se termine par e, laisser tomber le e et ajouter ing (sauf exception : be, see, flee, knee, etc.)

Si le verbe se termine par ie, remplacer ie par y et ajouter ing.

Pour les mots composés d'une consonne-voyelle-consonne, doubler la lettre finale avant d'ajouter ing.

Par défaut, il suffit d'ajouter ing"""

def make_ing_form(word):
    if word[-2:] == 'ie':
        word = word[:-2] + 'y'
        new_word = word + 'ing'

    elif word[-1:] == 'e':
        word = word[:-1]
        new_word = word + 'ing'

    elif len(word) == 3:
        new_word = word + word[-1] + 'ing'

    else:
        new_word = word + 'ing'

    return new_word

print(make_ing_form('lie'))
print(make_ing_form('see'))
print(make_ing_form('move'))
print(make_ing_form('run'))