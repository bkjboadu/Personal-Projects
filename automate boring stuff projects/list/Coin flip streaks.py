import random
numberOfStreaks= 0
streaks = 0
for experimentNumber in range(10000):
    outcomes = random.choices(['H','T'],k=100)
    for i in range(len(outcomes)):
        if outcomes[i] == outcomes[i-1]:
            streaks += 1
        else:
            streaks = 0

        if streaks == 6:
            numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))







