def filter_long_words(words, n):
    return [word for word in words if len(word) > n]

words_list = ["apple", "banana", "kiwi", "grapefruit", "fig"]
result = filter_long_words(words_list, 5)
print(result)  # 输出: ['banana', 'grapefruit']
