import requests
from bs4 import BeautifulSoup

#url = 'https://www.nytimes.com/2020/10/21/technology/personaltech/how-to-take-better-pet-portraits.html'
url = 'https://www.nytimes.com/2021/10/15/technology/elizabeth-holmes-trial-theranos-takeaways.html'

r = requests.get(url)

# r.encoding = 'utf-8'
print(r.headers.get("content-type", "unknown"))
print(r.encoding)
print(r)

soup = BeautifulSoup(r.text, 'html.parser')

ny = soup.findAll("p")
#print(ny)

for news_paragraph in ny:
	print(news_paragraph.get_text())

for news_image in soup.find_all('img'):
	print(news_image['src'])
