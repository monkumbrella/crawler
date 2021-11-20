import requests

'''
url = input('url: ')
file_name = input('file: ')

r = requests.get(url)

with open(file_name, 'w') as f:
    f.write(r.text)
    f.close()
'''

url = input('url: ')

r = requests.get(url)

#print(r.text)
#print(r.content)

with open('html_code.txt', 'w') as f:
	f.write(r.text)
	f.close()


