def sum(numbers):
    a = 0
    for num in numbers:
        a += num
    return a
def multiply(numbers):
    result = 1
    for num in numbers:
        result = result * num   # result *= num
    return result

print(sum([1, 2, 3, 4]))
print(multiply([1, 2, 3, 4]))