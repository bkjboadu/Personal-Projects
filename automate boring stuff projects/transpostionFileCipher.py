from transpositionEncrytDecrypt import encrypt,decrypt

def main():
    filename = input('>Please enter filename or directory:  ')
    mode = input('>Do you want to encrypt or decrypt: ')
    Key = input('Enter Key: ')
    while not Key.isdecimal():
        Key = input('Enter Key: ')
    Key = int(Key)
    while not mode.lower()[0] in ['e', 'd']:
        mode = input('Encrypt or Decrypt')
    inputfile = open(filename,'r')
    message = inputfile.read()
    if mode.lower().startswith('e'):
        translated = encrypt(message, Key)
    if mode.lower().startswith('d'):
        translated = decrypt(message, Key)
    output = open('done.txt','w')
    output.write(translated)
    output.close()
    inputfile.close()

if __name__ == '__main__':
    main()
