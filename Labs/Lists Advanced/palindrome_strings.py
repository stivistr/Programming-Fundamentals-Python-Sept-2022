words = input().split(' ')
palindrome = input()
palindrome_list = []
for word in words:
    if word == word[::-1]:
        palindrome_list.append(word)

counter = palindrome_list.count(palindrome)

print(palindrome_list)
print(f"Found palindrome {counter} times")