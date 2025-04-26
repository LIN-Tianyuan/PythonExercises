"""
def translate(word):
    a = ''
    for letter in word:
        if letter in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXZ':
            a = a + letter + 'o' + letter
        else:
            a = a + letter
    return a

print(translate('this is fun'))
"""
def translate(word):
    a = ''
    consonant = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXZ'
    for letter in word:
        if letter in consonant:
            a = a + letter + 'o' + letter
        else:
            a = a + letter
    return a

print(translate('this is fun'))