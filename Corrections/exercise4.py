def translate(text):
    result = ""
    vowels = "aeiouAEIOU"

    for char in text:
        if char.isalpha() and char not in vowels:
            result += char + "o" + char
        else:
            result += char
    return result

if __name__ == "__main__":
    print(translate("this is fun"))  # 输出 "tothohisos isos fofunon"

