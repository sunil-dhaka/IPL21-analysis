import requests
from bs4 import BeautifulSoup as bs

url='https://www.iplt20.com/points-table/men/2021'

r=requests.get(url)

soup=bs(r.text,'html.parser')
# print(soup.title.text)
# print(soup.find('table',class_='standings-table'))

teamNames=[team.find('span',class_='standings-table__team-name').text for team in soup.find_all('td',class_='standings-table__team')]

teamPoints=[team.text for team in soup.find_all('td',class_='standings-table__highlight')]

[print(name) for name in teamNames]
[print(name) for name in teamPoints]