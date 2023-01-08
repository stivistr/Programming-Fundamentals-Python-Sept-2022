dictionary_with_synonyms = {}
count_of_words = int(input())
list_of_words = []

for income in range(2 * count_of_words):
    word = input()
    list_of_words.append(word)

for synonym in range(0, len(list_of_words), 2):
    if list_of_words[synonym] not in dictionary_with_synonyms.keys():
        dictionary_with_synonyms[list_of_words[synonym]] = []
    dictionary_with_synonyms[list_of_words[synonym]].append(list_of_words[synonym + 1])

for key in dictionary_with_synonyms.keys():
    print(f"{key} - {', '.join(dictionary_with_synonyms[key])}")
