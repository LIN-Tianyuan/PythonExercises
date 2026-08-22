def isPalindrome(x):
    if x < 0:
        return False

    nombre = x
    inverse = 0

    while x > 0:
        chiffre = x % 10
        inverse = inverse * 10 + chiffre
        x = x // 10

    if nombre == inverse:
        return True
    else:
        return False


# Exemples
print(isPalindrome(-121))
print(isPalindrome(121))
print(isPalindrome(10))