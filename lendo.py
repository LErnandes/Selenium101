class Reader:
    def __init__(self, url):
        from selenium import webdriver
        import sys
        from bs4 import BeautifulSoup
        from random import uniform
        from time import sleep
        
        self.bmp = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

        options = webdriver.ChromeOptions()

        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url)
        self.soup = BeautifulSoup(self.driver.page_source, 'lxml')

        car = len(list(self.soup.text.replace('\n', '')))/3000
        imgs = len(self.soup.findAll('img'))/12
        s = car+imgs
        sleep(uniform(s-(s/30), s+(s/30)))

    def get(self, elem, clas):
        res = self.soup.findAll(elem, {'class': clas})
        res1 = []
        
        for y in range(len(res)):
            res1.append(res[y].text.translate(self.bmp))
        
        return res1

read = Reader("https://www.alexa.com/siteinfo/google.com")
re = read.get('span', 'num purple')

print(re)
