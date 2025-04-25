"""
Français:
Écrivez une fonction translate() qui traduira un texte en « rövarspråket » (langue des voleurs en suédois).
Cela signifie qu'il faut doubler chaque consonne et placer une occurrence de « o » entre les deux.
Par exemple, translate(« this is fun ») devrait renvoyer la chaîne « tothohisos isos fofunon ».
"""

def translate(word):
    ap = "bcdfghjklmnpqrstvwxz"
    for letters in word:
        if letters in ap:
            print(letters + "o" + letters, end="")
        else:
            print(letters, end= '')


translate('this is fun')