from bs4 import BeautifulSoup

f = open('sample.txt', 'rt')
source = f.read()
soup = BeautifulSoup(source, 'html.parser')
title_list = soup.find_all('td', class_='title')
for title in title_list:
    print(title.a.text)
f.close()

