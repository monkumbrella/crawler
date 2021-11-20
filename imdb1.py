import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

#url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"
url = 'https://www.imdb.com/search/title/?groups=top_1000&start=101&ref_=adv_nxt'
headers = {"Accept-Language": "en-US, en;q=0.5"}

r = req.get(url, headers=headers)

s = bs(r.text, "html.parser")
#print(s.prettify())

titles = []
years = []
times = []
ratings = []
metascores = []
votes = []
grosses = []

all_divs = s.find_all('div', class_='lister-item mode-advanced')  #all information in this div class tag

for one in all_divs:      #each one div tag
        title = one.h3.a.text
        titles.append(title)

        year = one.h3.find('span', class_='lister-item-year').text  #find method only return first match
        years.append(year)

        time = one.p.find('span', class_='runtime').text if one.p.find('span', class_='runtime').text else '-'
        times.append(time)

        rating = float(one.strong.text) #just use dot notation
        ratings.append(rating)

        score = one.find('span', class_='metascore').text if one.find('span', class_='metascore') else '-'
        metascores.append(score)

        vote_gross = one.find_all('span', attrs={'name': 'nv'})

        vote = vote_gross[0].text
        votes.append(vote)

        gross = vote_gross[1].text if len(vote_gross) > 1 else '-'
        grosses.append(gross)

#print(titles)
#print(years)
#print(times)
#print(ratings)
#print(metascores)
#print(votes)
#print(grosses)

data = pd.DataFrame({
'titles': titles,
'years': years,
'times': times,
'ratings': ratings,
'metascores': metascores,
'votes': votes,
'grosses': grosses,
})

print(data)
#print(data.dtypes)   show data type

data['years'] = data['years'].str.extract('(\d+)').astype(int)  #remove parentheses and convent to int
data['times'] = data['times'].str.extract('(\d+)').astype(int) #extract all digits in string
data['metascores'] = data['metascores'].str.extract('(\d+)')
data['metascores'] = pd.to_numeric(data['metascores'], errors='coerce')
#data['metascores'] = data['metascores'].astype(int)
data['votes'] = data['votes'].str.replace(',', '').astype(int)   #remove comma and convert to int
data['grosses'] = data['grosses'].map(lambda x: x.lstrip('$').rstrip('M'))
data['grosses'] = pd.to_numeric(data['grosses'], errors='coerce')
# pandad.to_numeric  convert to numeric type        cannot use .astype(float) to convert
#have dash '-'  it will return error  errors='coerce' will convert nonnumeric value dash to NaN(not a number)

#print(data['years'])
#print(data['times'])
print(data)
#print(data.dytypes)

#data.to_csv('imdb_1000top.csv')

