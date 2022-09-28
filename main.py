
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print('1) decrypt')
print('2) encrypt')
setting = input(':')

words = input('type your sentens:')

if setting == '2':
    encrypted = ''

    for word in words:
        letter_index = letters.index(word.upper()) + 1
        new_pos = letter_index + 13
        if new_pos <= 26:
            encrypted += letters[new_pos - 1]
        else:
            encrypted += letters[new_pos-27]

    print(encrypted)
else:
    decrypted = ''

    for word in words:
        letter_index = letters.index(word.upper()) + 1
        new_pos = letter_index - 13
        if new_pos >= 0:
            decrypted += letters[new_pos - 1]
        else:
            print(letter_index)
            print(new_pos)
            print(26 - abs(new_pos))
            decrypted += letters[25 - abs(new_pos)]
    print(decrypted)
