import requests
from bs4 import BeautifulSoup

url = 'http://www.g17.com.br/'

response = requests.get(url)

soup = BeautifulSoup(response.text)

links = [a['href'] for a in soup.find_all('a') if a['href'].count('g17.com.br/')]

materias = open('materias.txt', 'w')
for link in links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text)
    for text in [font.text for font in soup.find_all('font', {'class': 'texto-da-noticia'})[:-2]]:
        materias.writelines(text.strip().encode('utf-8').split('\n\n\n\n'))

materias.close()

