import random,sys
MAXLEN_OF_GUESS = 3
MAXNUM_OF_GUESS = 10

def main():
    print('''Bagels, a deductive logic game.
    By Bright Boadu brightboadujnr@gmail.com

    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:     That means:
          Pico          One digit is correct but in the wrong position
          Fermi         One digit is correct and in the right position
          Bagels        No digit is correct.

    For example, it the secret number was 248 and your guess was 843, the clues would be Fermi Pico.'''.format(MAXLEN_OF_GUESS))

    while True:
        secret = getSecret()
        print('I have thought up a number')
        print(' You have 10 guesses to get it')

        num_of_guess = 1
        while num_of_guess <= MAXNUM_OF_GUESS:
            guess = ''
            while len(guess) != MAXLEN_OF_GUESS or not guess.isdecimal():
                print('Guess #{}:'.format(num_of_guess))
                guess = input('> ')

            clues = getClues(guess,secret)
            print(clues)
            num_of_guess += 1

            if guess == secret:
                break
            if num_of_guess > MAXNUM_OF_GUESS:
                print('You are out of guess')
                print('The guess was {}'.format(secret))
        print('Do you want to play again?(yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing')

def getSecret():

    numbers = list('0123456789')
    random.shuffle(numbers)

    secret = ''
    for i in range(MAXLEN_OF_GUESS):
        secret += str(numbers[i])

    return secret

def getClues(guess,secret):
    if guess == secret:
        print('You got it')

    clues = []

    for i in range(MAXLEN_OF_GUESS):
        if guess[i] == secret[i]:
            clues.append('Fermi')
        elif guess[i] in secret:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()