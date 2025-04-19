"""
English:
Define a function sum() and a function multiply()
that sums and multiplies (respectively) all the numbers
in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10,
and multiply([1, 2, 3, 4]) should return 24.

Français:
Définissez une fonction sum() et une fonction multiply()
qui additionne et multiplie (respectivement) tous les nombres
d'une liste de nombres.
Par exemple, sum([1, 2, 3, 4]) doit renvoyer 10,
et multiply([1, 2, 3, 4]) doit renvoyer 24.

中文：
定义一个函数 sum() 和一个函数 multiply()，
分别对数字列表中的所有数字求和及相乘。
例如，sum([1, 2, 3, 4])应返回 10，
multiply([1, 2, 3, 4])应返回 24。
"""

def my_sum(numbers):
    return sum(numbers)

def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

# Test code
if __name__ == "__main__":
    print(my_sum([1, 2, 3, 4]))
    print(multiply([1, 2, 3, 4]))