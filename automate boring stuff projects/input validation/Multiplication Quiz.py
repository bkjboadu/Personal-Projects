import pyinputplus as pyip
import time, random

numberOfQuestion = 10
correctAnswer = 0

for questionNum in range(numberOfQuestion):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '%s. %s x %s = ' % (questionNum + 1,num1,num2)
    try:
        pyip.inputNum(prompt,allowRegexes=['^%s$' % (num1 * num2)],blockRegexes=['.*','Incorrect!!'],limit = 3, timeout = 9)
    except pyip.TimeoutException:
        print('Out of time')
    except pyip.RetryLimitException:
        print('Out of tries')
    else:
        print('Correct')
        correctAnswer += 1
    time.sleep(0.1)

print('%s / %s' % (correctAnswer,numberOfQuestion))




