import requests as req
from bs4 import BeautifulSoup as bs
from random import randint   #avoid ip banned
from time import sleep


'''
url = 'https://www.geeksforgeeks.org/page/1/'

r = requests.get(url)

soup = bs(r.text, 'html.parser')

titles = soup.find_all('div',attrs = {'class','head'})
print(titles[4].text)
'''


url = 'https://www.geeksforgeeks.org/page/'
for num in range(1,10):
	r = req.get(url + str(num) + '/')
	s = bs(r.text, 'html.parser')
	all_divs = s.find_all('div', attrs={'class','head'})
	for i in range(4,19):
		if num > 1:
			print(f"{(i-3)+num*15}" + all_divs[i].text)
		else:
			print(f"{i-3}" + all_divs[i].text)
	sleep(randint(2,10))


'''
url = ['https://www.geeksforgeeks.org', 'https://www.geeksforgeeks.org/page/10/']

for urls in range(0,2):
	r = requests.get(url[urls])
	soup = bs(r.text, 'html.parser')
	titles = soup.find_all('div', attrs={'class', 'head'})
	for i in range(4,19):
		if urls+1 > 1:
			print(f"{(i-3) + urls*15}" + titles[i].text)
		else:
			print(f"{i-3}" +  titles[i].text)
'''
