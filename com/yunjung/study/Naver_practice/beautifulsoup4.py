import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&nso=&where=blog&sm=tab_viw.all'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='api_text_lines')

print(title)