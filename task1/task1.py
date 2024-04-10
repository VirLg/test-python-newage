import requests
from bs4 import BeautifulSoup

url = 'https://docs.google.com/spreadsheets/d/1QX2IhFyYmGDFMvovw2WFz3wAT4piAZ_8hi5Lzp7LjV0/edit#gid=1902149593'

resp = requests.get(url).text
soup = BeautifulSoup(resp, "html.parser")
print('HTML',soup.a)
links = []
table = soup.find_all('a', class_='waffle-rich-text-link')
print(table)
