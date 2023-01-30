message = input('Enter the English message to translate into Pig Latin: ')
message = message.split(' ')
print(message)
result = []
for word in message:
    vowels = ['a', 'e', 'o', 'i', 'u', 'A', 'E', 'I', 'O', 'U']
    if not word[len(word) - 1].isalnum():
        suffix = word[len(word) - 1]
        word = word[:len(word) -1]
    else:
        suffix = ''

    if word[0] in vowels:
        new_word = word + 'yay' + suffix
        if word.istitle():
            new_word = new_word.title()
        elif word.isupper():
            new_word = new_word.upper()
        else:
            new_word = new_word.lower()
        result.append(new_word)
    elif not word[0].isalpha():
        result.append(word)
    elif word[0] and word[1] not in vowels:
        if len(word) < 3:
            new_word = word[1:] + word[0] + 'ay' + suffix
        else:
            new_word = word[2:] + word[:2] + 'ay' + suffix
        if word.istitle():
            new_word = new_word.title()
        elif word.isupper():
            new_word = new_word.upper()
        else:
            new_word = new_word.lower()
        result.append(new_word)
    else:
        new_word = word[1:] + word[0] + 'ay' + suffix
        if word.istitle():
            new_word = new_word.title()
        elif word.isupper():
            new_word = new_word.upper()
        else:
            new_word = new_word.lower()
        result.append(new_word)

piglatin = ' '.join(result)
print(piglatin)


