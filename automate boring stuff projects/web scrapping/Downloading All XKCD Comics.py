import webbrowser,requests,os,bs4
from pathlib import Path

os.makedirs('xkcd',exist_ok=True)
url = 'https://xkcd.com'
while not url.endswith('#'):
    #get homepage request text
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')

    comic_link = soup.select('#comic img')
    if comic_link == []:
        print('Could not find image to download')
    else:
        image_url = 'https:' + comic_link[0].get('src')
        print(image_url)
        res = requests.get(image_url)
        res.raise_for_status()

        image_file = open(Path('xkcd') / Path(image_url).name,'wb')

        for chunck in res.iter_content(100000):
            image_file.write(chunck)
        image_file.close()

        previous_link = soup.select('a[rel="prev"]')
        url = 'https://xkcd.com' + previous_link[0].get('href')

print('done')