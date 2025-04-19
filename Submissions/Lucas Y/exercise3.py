def find_longest_word(word_list):
    return max(len(word) for word in word_list)

if __name__ == "__main__":
    print(find_longest_word(["michael", "alex", "lucas", "luna", "luc"]))
    print(find_longest_word(["coca", "fanta", "spite", "seven up", "water", "oasis"]))
    print(find_longest_word(["cat", "dog", "crocodile", "elephant", "lion", "tiger"]))
