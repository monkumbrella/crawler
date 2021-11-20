from bs4 import BeautifulSoup as bs
import requests as req
'''  all urls use recursive
urls = []

def scrape(site):
	r = req.get(site)
	s = bs(r.text, 'html.parser')

	for i in s.find_all("a"):
		href = i.attrs['href']
		if href.startswith("/"):
			site = site + href
			if site not in urls:
				urls.append(site)
				print(site)
				scrape(site)

if __name__ =="__main__":
	site = "https://github.com/richardpenman/wswp_places"

	scrape(site)

'''
url = 'https://www.geeksforgeeks.org/'

r = req.get(url)

s = bs(r.text, 'html.parser')

'''
for link in s.find_all('a'):
	links = link.get('href')
	print(links)
'''

f = open('1.txt', 'w')
for link in s.find_all('a'):
	links = link.get('href')
	f.write(links)
	f.write("\n")
f.close()
