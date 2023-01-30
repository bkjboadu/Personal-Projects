import sys
import webbrowser
import bs4,requests

if len(sys.argv) > 1:
    search = ' '.join(sys.argv[1:])
else:
    search = 'goal.com'

url = 'https://www.google.com/search?q='

res = requests.get(url + str(search))
soup = bs4.BeautifulSoup(res.text,'html.parser')
links = soup.select("a[href]")
for link in links:
    try:
        webbrowser.open(link.get('href'))
        new = requests.get(link.get('href'))
        new.raise_for_status()
    except:
        print(str(link) + ' -->' + 'not found')