"""
def filter_long_words(word_list, n):
    max_word_list = []
    max_word = max(len(word) for word in word_list)
    if max_word > n:
        for word in word_list:
            if len(word) == max_word:
                max_word_list.append(word)
    else:
        return 0
    return max_word_list

print(filter_long_words(["michael", "alex", "lucas", "luna", "coca"], 4))
"""
def filter_long_words(word_list, n):
    max_word_list = []
    for word in word_list:
        if len(word) > n:
            max_word_list.append(word)
    return max_word_list

print(filter_long_words(["michael", "alex", "lucas", "luna", "coca"], 4))