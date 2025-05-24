def palindrome(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    alphabet_list = []
    for letter in sentence:
        if letter in alphabet:
            alphabet_list.append(letter)
    sentence_inverse = alphabet_list[::-1]
    if alphabet_list == sentence_inverse:
        print("It's a palindrome.")
    else:
        print("It's not a palindrome.")

palindrome("Step on no pets")
palindrome("Rise to vote sir")
palindrome("Dammit, I'm mad!")
palindrome("I love you.")
palindrome("Sstep on no petss")