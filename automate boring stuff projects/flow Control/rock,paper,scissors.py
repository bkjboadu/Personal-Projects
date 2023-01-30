import random
options = ['ROCK', 'PAPER', 'SCISSORS']
print(options)
print('0 Wins, 0 Losses, 0 Ties')
wins = 0
loss = 0
ties = 0
while True:
    com_choice = random.choice(options)
    my_choice = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ')
    print(my_choice, 'versus...')
    print(com_choice)
    if my_choice.lower() == com_choice.lower():
        print('It is a tie!')
        ties += 1
    elif my_choice.lower() == 'paper' and com_choice.lower() == 'scissors':
        loss += 1
        print('You loss!')
    elif my_choice.lower() == 'paper' and com_choice.lower() == 'rock':
        wins += 1
        print('You won!')
    elif my_choice.lower() == 'rock' and com_choice.lower() == 'scissors':
        wins += 1
        print('You won!')
    elif my_choice.lower() == 'rock' and com_choice.lower() == 'paper':
        loss += 1
        print('You lose!')
    elif my_choice.lower() == 'scissors' and com_choice.lower() == 'paper':
        wins += 1
        print('You won!')
    elif my_choice.lower() == 'scissors' and com_choice.lower() == 'rock':
        loss += 1
        print('You loss!')
    elif my_choice.lower() == 'quit':
        break
    print(f'{wins} Wins, {loss} Losses, {ties} Ties')



