import csv

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai').text
soup = BeautifulSoup(source, 'html.parser')

blokai = soup.find_all('div', class_ = 'card card__product card--anim js-product-compare-product')

for blokas in blokai:
    # print(blokas.text.strip().replace("\n", ""))

    name = blokas.find("a", class_= "mobiles-product-card_title js-open-product").text.strip()
    print(name)

    monthly_price = blokas.find("div", class_="mobiles-product-card_full-price price").text.strip()
    print(monthly_price)

    price = blokas.find("div", class_="mobiles-product-card_price-marker"0)

# with open("Telia Samsung telefonai.csv", "w", encoding="UTF-8", newline='') as failas:
#     csv_writer = csv.writer(failas)
#     csv_writer.writerow(['Modelis', 'Mėnesio kaina', 'Kaina'])

#     for blokas in blokai:
#         try:
#             pavadinimas = blokas.find('a', class_ = 'card__title js-product-name-truncate').text.strip()
#             men_kaina = blokas.find('div', class_ = 'pull-left').span.text.strip()
#             kaina = blokas.find('span', class_ = 'price--marker').next_element.next_element.next_element.next_element.span.text.strip()
#             csv_writer.writerow([pavadinimas, men_kaina, kaina])
#         except:
#             pass