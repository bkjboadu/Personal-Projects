
def main():
    message = 'Common sense is not so common.'
    key = 8

    encrypted = encrypt(message,key)

    print(encrypted)

def encrypt(message,key):
    ciphertext = [''] * key

    col = 0
    for letter in message:
        ciphertext[col] += letter
        col += 1

        if col == key:
            col = 0

    return ''.join(ciphertext)

if __name__ == '__main__':
    main()