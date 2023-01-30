import pyinputplus as pyip
import random

numberofQuestions = 10
correctAnswers = 0
for questionnumber in range(numberofQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s = '%(questionnumber,num1,num2)

    try:
        pyip.inputStr(prompt,allowRegexes=['^%s' % (num1 * num2)],blockRegexes=[('.*','Incorrect')],timeout=8,limit=3)
    except pyip.TimeoutException:
        print('Out of time')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1
