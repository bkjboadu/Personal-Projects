spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(x):
    result = ''
    for i in x:
        if i != x[-1]:
            result += str(i + ', ')
        else:
            result += str(' and ' + i)
    return result

print(comma_code(spam))

