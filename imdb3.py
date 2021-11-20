import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from time import sleep
from random import randint

headers = {"Accept-Language": "en-US,en;q=0.5"}

titles = []
years = []
times = []
ratings = []
metascores = []
votes = []
grosses = []

url = 'https://www.imdb.com/search/title/?groups=top_1000&start='

nums = np.arange(1, 1001, 50)

for num in nums:
  r = requests.get(url + str(num) + "&ref_=adv_nxt", headers=headers)

  s = bs(r.text, 'html.parser')
  all_divs = s.find_all('div', class_='lister-item mode-advanced')

  sleep(randint(2,10))

  for one in all_divs:

        title = one.h3.a.text
        titles.append(title)

        year = one.h3.find('span', class_='lister-item-year').text
        years.append(year)

        time = one.p.find('span', class_='runtime') if one.p.find('span', class_='runtime') else '-'
        times.append(time)

        rating = float(one.strong.text)
        ratings.append(rating)

        score = one.find('span', class_='metascore').text if one.find('span', class_='metascore') else '-'
        metascores.append(score)

        vote_gross = one.find_all('span', attrs={'name': 'nv'})

        vote = vote_gross[0].text
        votes.append(vote)

        gross = vote_gross[1].text if len(vote_gross) > 1 else '-'
        grosses.append(gross)

data = pd.DataFrame({
'titles': titles,
'years': years,
'ratings': ratings,
'metascores': metascores,
'votes': votes,
'grosses': grosses,
'times': times
})

data['years'] = data['years'].str.extract('(\d+)').astype(int)
data['times'] = data['times'].astype(str)
data['times'] = data['times'].str.extract('(\d+)').astype(int)
data['votes'] = data['votes'].str.replace(',', '').astype(int)
data['metascores'] = data['metascores'].str.extract('(\d+)')
data['metascores'] = pd.to_numeric(data['metascores'], errors='coerce')
# have dash  so cannot use .astype(float) to convert     it will return error
#errors='coerce' convert nonnumeric value  dash to NaN
data['grosses'] = data['grosses'].map(lambda x: x.lstrip('$').rstrip('M'))
data['grosses'] = pd.to_numeric(data['grosses'], errors='coerce')

print(data)
#print(data.dtypes)

#print(data.isnull().sum())   miss data

data.to_csv('information.csv')

