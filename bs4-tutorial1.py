import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# print(soup.title.text)

# print(soup)

# print(soup.p.text)

# print(soup.find_all('p'))

# for paragraph in soup.find_all('p'):
#    print(paragraph.text)


for url in soup.find_all('a'):
    print(url.get('href'))
