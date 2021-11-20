'''

some site do not allow requests
use user-agent && session(keep cookies)
some site require javascript to load page   need to use selenium   requests will not load javascript page
load page javascript first  then use requests

anti_bot: js
          captcha
          ip ban(ip proxy ip pool rotate ip)
          log in(some site only could access 1000 lines data after log in)
          user-agent
          asynchronous js and xml( browser with build-in js operations)
'''

'''
driver = webdriver.Chrome('/home/z/p/web_crawler/chromedriver')
driver.get('https://www.best-cd-price.co.uk/Keywords-229816/sex+pistols-1.html')
'''
#https://medium.com/quick-code/how-to-get-the-next-page-on-beautiful-soup-85b743750df4
#https://letslearnabout.net/python/beautiful-soup/your-first-web-scraping-script-with-python-beautiful-soup/
#https://www.best-cd-price.co.uk/?__cf_chl_jschl_tk__=pmd_dhiWXy3JPlTwxxHRxIlWmYStbgTGC6nBCEig5PyKQZw-1634802366-0-gqNtZGzNAiWjcnBszQaR
#https://www.best-cd-price.co.uk/Keywords-229816/sex+pistols-1.html?__cf_chl_jschl_tk__=pmd_56ieCME0eo0EbWFGCoE0t1vs2gcl8BBu6nYCG7XFbH0-1634802366-0-gqNtZGzNAmWjcnBszQgR


from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import lxml
import pandas as pd

#headers = {"User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"}

url = 'https://www.best-cd-price.co.uk/Keywords-229816/sex+pistols-1.html'    #cloudflare anti bot


#url = 'https://www.amazon.com/'

r = requests.get(url)
#r = requests.get(url, headers=headers)

'''session = requests.Session()
session.trust_env = False
r = session.get(url)
'''
print(r.status_code)


