import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Pause:
	def __init__(self, driver):
		self.driver = driver
		pass

	def pause(self, timer):
		action = ActionChains(self.driver)
		action.pause(timer)
		action.perform()



option = webdriver.EdgeOptions()
option.add_argument("start-maximized");
driver = webdriver.Edge(options = option)
page1='https://www.mpmadirectory.org.my/all-members?limit=200&cc=p'
driver.get(page1)

# retrieve the data from URL
response = requests.get(page1)

# parse the contents of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# filter all the <a> tags from the parsed document
for tag in soup.find_all('a'):
   print(tag)

Pause(driver).pause(10)
