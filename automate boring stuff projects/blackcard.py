'''Rules:
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.'''

import random,sys


#Set up the constants:
HEARTS = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES = chr(9824) # Character 9824 is '♠'.
CLUBS = chr(9827) # Character 982 is '♣'.
# (A list of chr codes is at ...)
BACKSIDE = 'backside'

def main():
    print(
    '''Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')

    money = 5000
    #check if player is out of money
    while True:
        if money <= 0:
            print('You are broke')
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

    #Let player enter their bet for this round
    print('Money:', money)
    bet = getBet(money)

    deck = getDeck()
    dealerhand = [deck.pop(), deck.pop()]
    playerhand = [deck.pop(), deck.pop()]

    while True:
        displayHand(playerhand,dealerhand,False)
        print()

        if getHandValue(playerhand) > 21:
            break

    # display player hand card
    # get player hand value
    # check if player bust
    # get player move
    # repeat till bust

def getBet(maxbet):
    while True: # Keep asking till the player provides a value
        print('How much do you bet?(1-{}, or QUIT'.format(maxbet))
        print()

        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            break

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= maxbet:
            return bet

def getDeck():
    deck = []
    for suit in (HEARTS,DIAMONDS,SPADES,CLUBS):
        for i in range(2,11):
            deck.append((str(i),suit))
        for j in ('K','Q','J','A'):
            deck.append((str(j),suit))
    random.shuffle(deck)
    return deck

def displayHand(playerHand,dealerHand,showDealerHand):
    '''Show the player's and dealer's cards. Hide the dealer's first'''
    if showDealerHand:
        print('Dealer:',getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('Dealer:', '???')
        displayCards([BACKSIDE] + dealerHand[1:])

    # Show the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    '''Return the total value of cards acquired'''
    value = 0
    numberOfAces = 0

    for card in cards:
        if card[0] == 'A':
            numberOfAces += 1
        elif card[0] in ('K','Q','J'):
            value += 10
        else:
            value += int(card[0])

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10

    return value

def displayCards(cards):
    '''Display all the cards in the card list'''
    row = ['','','',''] # The text to display on each row

    for i,card in enumerate(cards):
        row[0] += ' ___ ' # Print the top line of the card.
        if card == BACKSIDE:
            row[1] += '|## |'
            row[2] += '|###|'
            row[3] += '|_##|'
        else:
            rank, suit = card
            row[1] += '|{} |'.format(rank.ljust(2))
            row[2] += '| {} |'.format(suit)
            row[3] += '|_{}|'.format(rank.rjust(2,'_'))

    for row in row:
        print(row)


def getMove(playerHand,money):
    while True:
        moves = ['(H)it','(S)tand']

        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move:
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H','S'):
            return move # Player has entered a valid move.
        if move == 'D' and '(D)ouble down' in moves:
            return move # Player has entered in valid move