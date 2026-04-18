"""
Français:
Définissez une fonction sum() et une fonction multiply()
qui additionne et multiplie (respectivement) tous les nombres
d'une liste de nombres.
Par exemple, sum([1, 2, 3, 4]) doit renvoyer 10,
et multiply([1, 2, 3, 4]) doit renvoyer 24.
"""

def sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
print(sum([1,4,6]))

def multyply(numbers):
    total = 1
    for n in numbers:
        total *= n
    return total
print(multyply([5,6]))
