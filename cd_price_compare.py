from bs4 import BeautifulSoup as bs
import requests as req
import lxml
import pandas as pd

band_name = input('Please, enter a band name:\n')
formated_band_name = band_name.replace(' ', '+')
print(f'Searching {band_name}. Wait, please...')

base_url = 'http://www.best-cd-price.co.uk'
search_url = f'http://www.best-cd-price.co.uk/Keywords-229816/{formated_band_name}-1.html'

page = req.get(search_url)

if page.status_code == req.codes.ok:
  s = bs(page.text, 'lxml')
  list_all_cd = s.findAll('li', class_='ResultItem')
  data = {
    'Image': [],
    'Name': [],
    'URL': [],
    'Artist': [],
    'Binding': [],
    'Format': [],
    'Release Date': [],
    'Label': [],
  }

  for cd in list_all_cd:

    # Getting the CD attributes
    image = cd.find('img', class_='ProductImage')['src']

    name = cd.find('h2').find('a').text

    url = cd.find('h2').find('a')['href']
    url = base_url + url

    artist = cd.find('li', class_="Artist")
    artist = artist.find('a').text if artist else ''

    binding = cd.find('li', class_="Binding")
    binding = binding.text.replace('Binding: ', '') if binding else ''

    format_album = cd.find('li', class_="Format")
    format_album = format_album.text.replace('Format: ', '') if format_album else ''

    release_date = cd.find('li', class_="ReleaseDate")
    release_date = release_date.text.replace('Released: ', '') if release_date else ''

    label = cd.find('li', class_="Label")
    label = label.find('a').text if label else ''

    # Store the values into the 'data' object
    data['Image'].append(image)
    data['Name'].append(name)
    data['URL'].append(url)
    data['Artist'].append(artist)
    data['Binding'].append(binding)
    data['Format'].append(format_album)
    data['Release Date'].append(release_date)
    data['Label'].append(label)

  table = pd.DataFrame(data, columns=['Image', 'Name', 'URL', 'Artist', 'Binding', 'Format', 'Release Date', 'Label'])
  table.index = table.index + 1
  table.to_csv(f'{band_name}_albums.csv', sep=',', encoding='utf-8', index=False)
  print(table)
