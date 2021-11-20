from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

'''
driver = webdriver.Chrome('/home/z/Downloads/chromedriver')

url = 'https://hoopshype.com/salaries/players/'

driver.get(url)

players = driver.find_elements_by_xpath('//td[@class="name"]')

palyers_list = []

for p in range(len(players)):

	palyers_list.append(players[p].text)

print(palyers_list)
'''
#df = pd.DataFrame(columns=['Player','Salary','Year']) # creates master dataframe

driver = webdriver.Chrome('/home/z/p/web_crawler/chromedriver')

url = 'https://hoopshype.com/salaries/players/'

driver.get(url)

players = driver.find_elements_by_xpath('//td[@class="name"]')
salaries = driver.find_elements_by_xpath('//td[@class="hh-salaries-sorted"]')

players_list = []

for p in range(len(players)):
	players_list.append(players[p].text)

print(players_list)

salaries_list = []

for s in range(len(salaries)):
	salaries_list.append(salaries[s].text)

print(salaries_list)

driver.close()

