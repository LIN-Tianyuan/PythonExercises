"""
Français:
Définissez une fonction sum() et une fonction multiply()
qui additionne et multiplie (respectivement) tous les nombres
d'une liste de nombres.
Par exemple, sum([1, 2, 3, 4]) doit renvoyer 10,
et multiply([1, 2, 3, 4]) doit renvoyer 24.
"""
def sum(numbers):
    o = 0
    for y in numbers:
        o += y
    return o

def multiply(numbers):
    d = 1
    for c in numbers:
        d *= c
    return d

o = sum([1, 2, 3, 4])
d = multiply([1, 2, 3, 4])
print(o)
print(d)