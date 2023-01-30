import time
print('Enter number:')
x = input()
while not x.isdecimal() or x == '0':
    print('You need to enter a number and it should be greater than 0')
    x = input()

def collatz(x):
    x = int(x)
    while x != 1:
        print(x)
        if x % 2 == 0:
            x = x // 2
        elif x % 2 == 1:
            x =  (3 * x) + 1
        time.sleep(0.1)
    print(x)
collatz(x)
