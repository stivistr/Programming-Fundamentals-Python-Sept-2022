words = input().split()
words_count = {}

for word in words:
    if word.lower() not in words_count:
        words_count[word.lower()] = 0
    words_count[word.lower()] += 1

for key_word in words_count.keys():
    if words_count[key_word] % 2 != 0:
        print(key_word, end=' ')
