import datetime,random


def getbirthday(numberOfBday):
    birthdays = []
    for i in range(numberOfBday):
        startOfYear = datetime.date(2001,1,1)
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    else:
        for a,birthdayA in enumerate(birthdays):
            for b,birthdayB in enumerate(birthdays[a+1:]):
                if birthdayA == birthdayB:
                    return birthdayA


while True:
    print('how many birthdays shall i generate?(Max 100)')
    response = input('> ')
    if response.isdecimal() and (0<int(response)<100):
        numBdays = int(response)
        break

MONTHS = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep',
          'Oct','Nov','Dec')

print('Here are',str(numBdays),'birthdays')
birthdays = getbirthday(numBdays)
for i,birthday in enumerate(birthdays):
    if i != 0:
        #Display a coma for each birthday after the first birthday.
        print(', ',end='')
    MONTH = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(MONTH,birthday.day)
    print(dateText,end='')

print('\nIn this simulation, ',end='')
match = getMatch(birthdays)
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName,match.day)
    print('multiple people have a birthday on',dateText)
else:
    print('there are no matching birthdays.')
print()

print('Generating',str(numBdays),'random birthdays 100,000 times...')
input('Please Enter to begin...')
print('Let\'s run another 100,000 simulations.')

simMatch = 0
for i in range(100000):
    if i % 10000 == 0:
        print(i,'simulations run...')
    birthdays = getbirthday(numBdays)
    if getMatch(birthdays) != None:
        simMatch += 1
probability = round(int(simMatch)/100000 * 100,2)
print('Out of 100,000 simulations of',str(numBdays), 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that',str(numBdays), 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')




