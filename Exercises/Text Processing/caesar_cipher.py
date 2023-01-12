non_crypred_text = input()
crypted_version = ''
for char in range(len(non_crypred_text)):
    crypted_version += chr(ord(non_crypred_text[char]) + 3)
print(crypted_version)
