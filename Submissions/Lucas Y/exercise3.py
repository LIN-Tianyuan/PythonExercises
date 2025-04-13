def find_longest_word(word_list):
    return max(len(word) for word in word_list)


print(find_longest_word(["coca", "michael", "alex", "lucas", "luna", "luc"]))