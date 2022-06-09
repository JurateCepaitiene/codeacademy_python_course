# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.delfi.lt/').text
# print(source)

# soup = BeautifulSoup(source, 'html.parser')
# blokas = soup.find("div", class_ = 'headline')
# print(blokas)
# print("======")
# blokas = soup.find("h3", class_ = 'headline-title')
# blokas = blokas.find()
# print(blokas.prettify())

# situo budu issikirpau konkrecius zodzius

# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokas = soup.find('div', class_ = 'headline')

# kategorija = blokas.find('div', class_ = 'headline-category').text.strip()

# tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
# print(kategorija)
# print(tekstas)

# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokai = soup.find_all('div', class_ = 'headline')

# for blokas in blokai:
#     try:
#         kategorija = blokas.find('div', class_ = 'headline-category').text.strip()
#         tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
#         print(kategorija)
#         print(tekstas)
#     except:
#         pass

# iskerpa visus headline'us

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')
blokai = soup.find_all('div', class_ = 'headline')

with open("delfi naujienos.csv", "w", encoding="UTF-8", newline='') as failas:

    csv_writer = csv.writer(failas)
    csv_writer.writerow(['Kategorija', 'Tekstas'])
    for blokas in blokai:
        try:
            kategorija = blokas.find('div', class_ = 'headline-category').text.strip()
            tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
            csv_writer.writerow([kategorija, tekstas])
        except:
            pass