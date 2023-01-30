import requests,bs4,pyperclip,sys,os
from pathlib import Path
if len(sys.argv) > 1:
    keyword = ' '.join(sys.argv[1:])
else:
    keyword = 'lion'

os.makedirs('imgur',exist_ok=True)
url = 'https://imgur.com/search?q='
res = requests.get(url + keyword)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
links = soup.select('.post > .image-list-link img')
for i in range(len(links)):
    new_url = 'https:' + links[i].get('src')
    res = requests.get(new_url)
    res.raise_for_status()
    file_name = str(Path('imgur') / Path(new_url).name)
    image_file = open(file_name,'wb')
    for chunks in res.iter_content(100000):
        image_file.write(chunks)
    image_file.close()



