from bs4 import BeautifulSoup as bs
import requests as req
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''page = 1
while page != 6:
      url = f"https://www.bookdepository.com/bestsellers?page={page}"
      print(url)
      page = page + 1
'''

'''page = 1
titles = []

while page != 35:
	url = f"https://www.bookdepository.com/bestsellers?page={page}"
	r = req.get(url)
	s = bs(r.content, 'lxml')
	for h3 in s.find_all("h3", class_="title"):
		titles.append(h3.get_text(strip=True))
	page = page + 1

print(len(titles))

for title in titles[:6]:
	print(title)
'''

'''
#https://data36.com/scrape-multiple-web-pages-beautiful-soup-tutorial/
page = 1
formats_all = []

while page != 35:
	url = f"https://www.bookdepository.com/bestsellers?page={page}"
	r = req.get(url)
	s = bs(r.content, 'lxml')
	formats_page = s.select("div.item-info p.format")
	for product_format in formats_page:
		formats_all.append(product_format.get_text())
	page = page + 1
formats_series = pd.Series(formats_all)
formats_series.value_counts()
'''
