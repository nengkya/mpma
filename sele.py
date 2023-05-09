import re
import requests
from bs4 import BeautifulSoup


page1='https://www.mpmadirectory.org.my/all-members?limit=200&cc=p'

#retrieve the data from URL
response = requests.get(page1)

#parse the contents of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

#filter all the <a> tags from the parsed document
for a in soup.find_all('a'):
	print(a.get('href'))
