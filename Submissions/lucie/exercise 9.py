""""
Etant donné un tableau d'entiers, nums, et une cible,
trouver les deux entiers dans le tableau dont la somme est la cible et
retourner leurs indices de tableau.
"""""

def two_indices(nums, cible):
    # nums= [2,11,15,7]
    #cible=9
    #len(nums)=4
    #for i in range(4): O à 3
    for i in range(len(nums)):
        #for j in range (i+1,4):1 à 4
        for j in range(i + 1, len(nums)):
            #i =0
            #num[j]=7
            #cible= 9
            if nums[i] + nums[j] == cible:
                #[0,1]
                return [i, j]
    return None

liste = [2, 7, 11, 15]
cible = 9

print(two_indices(liste, cible))