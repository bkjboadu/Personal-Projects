import pyperclip,re
phoneregs = re.compile(r'(\d{3}|\(\d{3}\))[-*\s\.](\d{3})[-*\s\.](\d{4})')
emailregs = re.compile(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,4}',re.VERBOSE)
text = str(pyperclip.paste())
matched = []
for group in phoneregs.findall(text):
    print(group)
    matched.append('-'.join([group[0],group[1],group[2]]))


for y in emailregs.findall(text):
    matched.append(y)

if len(matched) != 0:
    list = '\n'.join(matched)
    print(list)
    pyperclip.copy(list)
else:
    print('matches not found')
