number = int(input())
word = input()

list_of_all_words = []
list_with_word = []

for num in range(number):
    current_word = input()
    list_of_all_words.append(current_word)
    if word in current_word:
        list_with_word.append(current_word)

print(list_of_all_words)
print(list_with_word)