import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import os

url = 'https://www.basketball-reference.com/leagues/NBA_2020_per_game.html'

r = req.get(url)

s = bs(r.content, 'html.parser')
#print(s.prettify())

table = s.find_all(class_="full_table")
#print(table)

head = s.find(class_="thead")
column_names_raw = [head.text for item in head][0]
column_names_clean = column_names_raw.replace("\n",",").split(",")[2:-1]
#print(head)
#print(column_names_raw)
#print(column_names_clean)

players = []

for i in range(len(table)):
	player = []

	for td in table[i].find_all("td"):
		player.append(td.text)

df = pd.DataFrame(players, columns = column_names_raw).set_index("Player")

#df.index = df.index.str.replace('*', '')

print(df)
