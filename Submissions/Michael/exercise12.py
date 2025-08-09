def prefix(strs: list):
    first = strs[0]
    pre = ""
    for i in range(len(first)):
        letter = first[i]
        for mot in strs[1:]:
            if i >= len(mot) or mot[i] != letter:
                return pre
        pre += letter

    return pre


print(prefix(["flower", "flow", "flight"]))
print(prefix(["dog", "racecar", "car"]))
