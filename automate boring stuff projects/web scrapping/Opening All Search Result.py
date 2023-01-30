import webbrowser,sys,requests,bs4,pyperclip

if len(sys.argv) > 1:
    search = ' '.join(sys.argv[1:])
else:
    search = 'numpy'

url = 'https://pypi.org/search/?q=%s' % (search)
res = requests.get(url)
res.raise_for_status()

egsoup = bs4.BeautifulSoup(res.text,'html.parser')
elems = egsoup.select('.package-snippet')
for i in elems:
    unique_url = 'https://pypi.org/%s' % (i.get('href'))
    webbrowser.open(unique_url)

