from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.delfi.lt/news/daily/world/karas-ukrainoje-rusu-ziniasklaida-ukrainoje-suciuptiems-britams-ir-marokieciui-mirties-bausme.d?id=90439595').text
print(source)

soup = BeautifulSoup(source, 'html.parser')
# blokas = soup.find("div", class_ = 'delfi-article-lead'.text.strip())
blokai = soup.find_all("p")
# print(blokas.prettify())
# print(blokai[:8])

blokai = blokai[1:8]
# print(type(blokai))

for blokas in blokai:
    print(blokas.text.strip())



