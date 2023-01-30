import bs4,requests,webbrowser,sys,pyperclip

if len(sys.argv) > 1:
    on_search = ' '.join(sys.argv[1:])
else:
    on_search = pyperclip.paste()

search = requests.get('https://www.google.com/search?q=' + on_search)
print(search.raise_for_status())
Soup = bs4.BeautifulSoup(search.text,'html.parser')
search_results = Soup.select('.yuRUbf a')
if search_results == []:
    print('no results link found')
else:
    numOpen = min(5,len(search_results))
    for i in range(numOpen):
        search_results_link = search_results[i].get('href')
        webbrowser.open(search_results_link)