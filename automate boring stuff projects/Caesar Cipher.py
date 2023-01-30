
def main():
    # Get text and their keys
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Text = input('Please enter text to encrypt or decrypt:')
    Key = input('input encryption key:')
    while not Key.isdecimal() and str(Key).lower()[0] not in ['u','n']:
        Key = input('Key must bet a number or unknown:')
    if Key.isdecimal():
        Key = int(Key)
    # State whether they should be encrypted of decrypted
    mode = input('Encrypt or Decrypt:')
    while mode.lower()[0] not in ['e','d']:
        mode = input('Encrypt or Decrypt:')
    # Executed task as requested
    if str(Key).lower()[0] in ['n','u'] and mode.lower().startswith('d'):
        bruteForceAttack(Text,LETTERS)
    elif mode.lower().startswith('e'):
        encypt(Text,Key,LETTERS)
    elif mode.lower().startswith('d'):
        decrypt(Text,Key,LETTERS)



def encypt(Text,Key,LETTERS):
    translated = '' # final product
    for letter in Text:
        if letter not in LETTERS:
            translated += str(letter)
            continue
        letter_index = LETTERS.find(letter)
        new_value = int(letter_index) + Key
        if new_value >= len(LETTERS):
            new_value -= len(LETTERS)
        translated += LETTERS[new_value]
    print(translated)



def decrypt(Text,Key,LETTERS):
    translated = ''
    for letter in Text:
        if letter not in LETTERS:
            translated += str(letter)
            continue
        letter_index = LETTERS.find(letter)
        new_value = int(letter_index) - Key
        if new_value < 0:
            new_value += len(LETTERS)
        translated += LETTERS[new_value]
    print(translated)

def bruteForceAttack(message,LETTERS):
    from textblob import TextBlob
    for key in range(len(LETTERS)):
        translated = ''
        for letter in message:
            if letter in LETTERS:
                num = LETTERS.find(letter)
                num -= key

                if num < 0:
                    num += len(LETTERS)
                    translated += LETTERS[num]
                else:
                    translated += LETTERS[num]
            else:
                translated += letter
        if TextBlob(translated).detect_language() == 'en':
            print(translated)



if __name__ == '__main__':
    main()