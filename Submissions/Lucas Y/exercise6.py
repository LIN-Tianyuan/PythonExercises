def pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = []
    sentence = sentence.lower()

    for letter in sentence:
        if letter in alphabet:
            if letter not in alphabet_list:
                alphabet_list.append(letter)

    if len(alphabet_list) == 26:
        print("It's a pangram.")
    else:
        print("It's not a pangram.")


pangram("The quick brown fox jumps over the lazy dog.")
pangram("J'aime les chien vvvv")