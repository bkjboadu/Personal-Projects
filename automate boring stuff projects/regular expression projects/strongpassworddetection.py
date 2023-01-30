import re
import pyperclip

len_regex = re.compile(r'.{8,}')
lower_case = re.compile(r'[a-z]+')
upper_case = re.compile(r'[A-Z]+')
digit_regex = re.compile(r'[0-9]+')

password = input('Please enter password: ')
if len_regex.search(password) and lower_case.search(password) and upper_case.search(password) and digit_regex.search(password):
    print('password is strong')
else:
    print('Password isn\'t strong')


