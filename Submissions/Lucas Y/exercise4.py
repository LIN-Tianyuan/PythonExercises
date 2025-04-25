def translate(word):
    a = ''
    # letter = 'o'
    for consonant in word:
        if consonant in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXZ':
            a = a + consonant + 'o' + consonant  # 'o' = letter
        else:
            a = a + consonant
    return a


print(translate('this is fun'))