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


def load(link):
    latauslinkki = 'https://www.vero.fi'+link
    print(latauslinkki)



sana = ('')
x = input('Vuosimalli:')

for i in (dwn_1[3]):
    sana = sana+i
    if x in sana:
        load(dwn_1[3])
        break
    else:
        continue

index = 0

for solu in dwn_1:
    for i in (dwn_1[index]):
        sana = sana + i
        if x in sana[index:]:
            load(dwn_1[index])
            break
        else:
            continue
    index = index + 1
else:
    index = index + 1

print(sana)


print(dwn_1[3])

sd = '2014'
sana1 = ''

for i in dwn_1[3]:
    if i in sd:
        sana1 = sana1 + i
        if sana == sd:
            break
        else:
            continue


print('Täs se on :', sana1)