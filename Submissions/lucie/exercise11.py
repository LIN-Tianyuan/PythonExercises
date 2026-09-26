def romanToInt(s: str) -> int:

    romains = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and romains[s[i]] < romains[s[i + 1]]:

            total += romains[s[i + 1]] - romains[s[i]]
            i += 2
        else:
            total += romains[s[i]]
            i += 1
    return total