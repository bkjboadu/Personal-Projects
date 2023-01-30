import math

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myMessage,myKey)

    print(plaintext + '|')

def decryptMessage(myMessage,myKey):
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
        print(plaintext)

    return ''.join(plaintext)


if __name__ == '__main__':
    main()