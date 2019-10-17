from selenium import webdriver
from bs4 import BeautifulSoup
import sys

bmp = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#options = webdriver.Chrome()

#options.add_argument('headless')
#options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome()
driver.get("https://www.alexa.com/siteinfo/google.com")

soup = BeautifulSoup(driver.page_source, 'lxml')
res = soup.findAll('span', {'class': 'num purple'})

print('Search Traffic: ' + res[0].text.translate(bmp))
print('Bounce Rate: ' + res[1].text.translate(bmp))
