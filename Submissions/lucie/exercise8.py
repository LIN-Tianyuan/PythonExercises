def make_ing_form(verb):
    vowels = "aeiou"

    if len(verb) >= 2:
        if verb[-2] == "i" and verb[-1] == "e":
            return verb[:-2] + "ying"

    if len(verb) >= 1:
        if verb[-1] == "e":
            return verb[:-1] + "ing"

    if len(verb) >= 3:
        a = verb[-3]
        b = verb[-2]
        c = verb[-1]

        if a not in vowels:
            if b in vowels:
                if c not in vowels:
                    return verb + c + "ing"

    return verb + "ing"

print(make_ing_form("lie"))
print(make_ing_form("see"))
print(make_ing_form("move"))
print(make_ing_form("hug"))   #