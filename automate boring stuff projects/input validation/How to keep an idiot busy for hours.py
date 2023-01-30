import pyinputplus as pyip

while True:
    print('Want to know how to keep an idiot busy for hours?')
    question = pyip.inputYesNo()
    if question != 'no':
        continue
    print('Thank you. Have a nice day')
    break

