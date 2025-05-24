def is_palindrome(phrase):
    cleaned = ''.join(char.lower() for char in phrase if char.isalnum())
    return cleaned == cleaned[::-1]


print(is_palindrome("Go hang a salami I'm a lasagna hog."))  # True
print(is_palindrome("Was it a rat I saw?"))                  # True
print(is_palindrome("Hello, world!"))                        # False
print(is_palindrome("Dammit, I'm mad!"))                     # True
