import  requests
from bs4 import BeautifulSoup

page = requests.get('https://dialpadbeta.com/csr/applog/5203124005109760')
soup = BeautifulSoup(page.content,'html.parser')
print (soup)


