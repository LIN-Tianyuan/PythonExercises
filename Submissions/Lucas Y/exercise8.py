def make_ing_form(word):
    if word[-2:] == 'ie':
        word = word[:-2] + 'y'
        new_word = word + 'ing'

    elif word[-1:] == 'e':
        word = word[:-1]
        new_word = word + 'ing'

    elif len(word) == 3:
        new_word = word + word[-1] + 'ing'

    else:
        new_word = word + 'ing'

    return new_word

print(make_ing_form('lie'))
print(make_ing_form('see'))
print(make_ing_form('move'))
print(make_ing_form('run'))