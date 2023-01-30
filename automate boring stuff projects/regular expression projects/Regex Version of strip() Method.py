import re

def strip(text,remove = ' '):
    remove_begin = re.compile(r'^[%s]' % remove)
    remove_end = re.compile(r'[%s]$' % remove)
    text = remove_begin.sub('',text)
    text = remove_end.sub('',text)
    print(text)

text = input('Please enter text to strip: ')
strip_value = input('Please enter what you want to strip: ')

strip(text,strip_value)