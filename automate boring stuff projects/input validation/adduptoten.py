import pyinputplus as pyip

def adduptoten(numbers):
    numbers = str(numbers)
    sum = 0
    for i in range(len(numbers)):
        number = int(numbers[i])
        sum += number
    if sum != 10:
        raise Exception('Numbers should add up to 10 not %s' % sum)
    return int(numbers)

print('enter your numbers:')
response = pyip.inputCustom(adduptoten)
print(response)