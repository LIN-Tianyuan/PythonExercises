""""
Etant donné un tableau d'entiers, nums, et une cible,
trouver les deux entiers dans le tableau dont la somme est la cible et
retourner leurs indices de tableau.
"""""

def two_indices(nums, cible):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == cible:
                return [i, j]
    return None

liste = [2, 7, 11, 15]
cible = 9

print(two_indices(liste, cible))