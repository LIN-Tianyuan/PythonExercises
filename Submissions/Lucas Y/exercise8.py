"""
English:
In English, the present participle is formed by adding the suffix -ing
to the infinite form: go -> going. A simple set of heuristic rules can be given as follows:

If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)

If the verb ends in ie, change ie to y and add ing

For words consisting of consonant-vowel-consonant, double the final letter before adding ing

By default just add ing

Your task in this exercise is to define a function make_ing_form()
which given a verb in infinitive form returns its present participle form.
Test your function with words such as lie, see, move and hug.
However, you must not expect such simple rules to work for all cases.

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


"""def make_ing_form(word):
    if word[-1:] == 'e':
        word = word.removesuffix('e')
        new_word = word.__add__('ing')
        if word[-2:] == 'ie':
            print(new_word)
    print(word[-1:])
    print(word[-2:])


make_ing_form('lie')"""


def make_ing_form(word):
    if word[-2:] == 'ie':
        word = word[:-2] + 'y'
        new_word = word + 'ing'

    if word[-1:] == 'e':
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