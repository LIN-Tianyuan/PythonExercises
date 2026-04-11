def sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result
print(sum([1, 2, 3,5]))
print(multiply([1, 2, 3, 4]))