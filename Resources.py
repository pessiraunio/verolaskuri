from bs4 import BeautifulSoup
import requests
import re


#Määritetään polku josta latauslinkit haetaan

source = requests.get('https://www.vero.fi/henkiloasiakkaat/auto/autoverotus/autoveron_maara/taulukoita_ajoneuvojen_sovelletuista_ve/').text

#Soup muuttujaan tallennetaan sourcen paresettauna lxml:llä
soup = BeautifulSoup(source, 'lxml')

#Navigoidaan html:ssä oikeaan kohtaan
main_body = soup.find('div', class_='main-body')

#Etsitään linkit html:stö

dwn_1 = []

for i in main_body.find_all('a', href=re.compile('download')):
    dwn_1.append(i['href'])


dwn_2 = []

for i in main_body.find_all('a', href=re.compile('contentassets')):
    dwn_2.append(i['href'])


def lataa(link):

    latauslinkki = 'https://www.vero.fi'+link

    return print(latauslinkki)

lataa(dwn_1[0])