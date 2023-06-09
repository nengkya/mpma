import re
import logging
import requests
from bs4 import BeautifulSoup


def get_soup(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	return soup


page1='https://www.mpmadirectory.org.my/all-members?limit=200&cc=p'
soup = get_soup(page1)

logging.basicConfig(filename = 'company.log', level = logging.INFO)

i = 1
#filter all the <a> tags from the parsed document
for a in soup.find_all('a'):
	a = a.get('href')

	if not ('/members/' in a):
		continue

	if i == 4:
		url = 'https://www.mpmadirectory.org.my' + a
		soup = get_soup(url)
		logging.info(soup)
		print(type(soup.text))

	i += 1
