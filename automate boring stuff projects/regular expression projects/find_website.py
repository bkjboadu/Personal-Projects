import re,pyperclip

urlsregex = re.compile(r'''(
(http) #http
s?
(://[a-zA-Z]+)
(\.[a-z]{2,4})
)''',re.VERBOSE)
text = '''https://facebook.com and http://google.com and so what is theat you were saying https://amazon.web'''
match = []
for url in urlsregex.findall(text):
    match.append(url[0])
print('\n'.join(match))