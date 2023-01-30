import math

def main():
    message = input('Enter text to encrypt or decrypt: ')
    Key = input('Enter Key: ')
    while not Key.isdecimal():
        Key = input('Enter Key: ')
    Key = int(Key)
    encrypting = input('Encrypt or Decrypt: ')
    while not encrypting.lower()[0] in ['e','d']:
        encrypting = input('Encrypt or Decrypt')
    if encrypting.lower().startswith('e'):
        translated = encrypt(message,Key)
    if encrypting.lower().startswith('d'):
        translated = decrypt(message,Key)
    print(translated + "|")

def encrypt(message,key):
    ciphertext = [''] * key

    col = 0
    for letter in message:
        ciphertext[col] += letter
        col += 1

        if col == key:
            col = 0

    return ''.join(ciphertext)

def decrypt(myMessage,myKey):
    numOfCol = math.ceil(len(myMessage) / myKey)
    numOfRow = myKey
    numOfShaded = (numOfRow * numOfCol) - len(myMessage)

    plaintext = [''] * numOfCol

    col = 0
    row = 0
    for symbol in myMessage:
        plaintext[col] += symbol
        col += 1

        if (col == numOfCol) or (col == numOfCol - 1 and row >= numOfRow - numOfShaded):
            col = 0
            row += 1

    return ''.join(plaintext)

if __name__ == '__main__':
    main()

