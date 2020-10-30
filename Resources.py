from bs4 import BeautifulSoup
import requests


source = requests.get('https://www.vero.fi/henkiloasiakkaat/auto/autoverotus/autoveron_maara/taulukoita_ajoneuvojen_sovelletuista_ve/').text

soup = BeautifulSoup(source, 'lxml')

main_body = soup.find('div', class_='main-body')

a = main_body.find_all('a')

for index in a:
    if filter(lambda x: ('vuosi') in x, index):

        print(index)
    else:
        continue




