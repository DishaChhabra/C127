from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'

#webdriver.Edge
browser = webdriver.Chrome('./chromedriver.exe')
browser.get(url)
time.sleep(10)
def get_data():
    headers = ['NAME',	'LIGHT-YEARS FROM EARTH',	'PLANET MASS',	'STELLAR MAGNITUDE',   'DISCOVERY DATE']
    data = []
    for i in range(0,10):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for a in soup.find_all('ul', attrs={'class','exoplanet'}):
            li = a.find_all('li')
            temp = []
            for w,o in enumerate(li):
                if w == 0:
                    temp.append(o.find_all('a')[0].contents[0])
                else:
                    temp.append(o.contents[0])
            data.append(temp)
        browser.find_element('xpath','//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()
    with open('data.csv', 'w') as file:
        Writer = csv.writer(file)
        Writer.writerow(headers)
        Writer.writerows(data)  

get_data()
