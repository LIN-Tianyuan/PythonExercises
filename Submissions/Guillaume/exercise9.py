"""Français:
Etant donné un tableau d'entiers, nums, et une cible,
trouver les deux entiers dans le tableau dont la somme est la cible et
retourner leurs indices de tableau."""


def trouver_indices(nums, cible):

    for i in range(len(nums)):


        for j in range(i + 1, len(nums)):


            if nums[i] + nums[j] == cible:

                return [i, j]



mes_nombres = [2, 7, 11, 15]
ma_cible = 9

resultat = trouver_indices(mes_nombres, ma_cible)
print(f"Les indices sont : {resultat}")