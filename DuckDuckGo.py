# Usage --
    # pip install selenium
    # python DuckDuckGo.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import os

os.system('cls' if os.name == 'nt' else 'clear')

Query = input('Enter Your Query : ')
Pages = int(input('Enter No. Of Pages : '))

driver = webdriver.Chrome()
driver.get(f"https://duckduckgo.com/?va=j&t=hc&q={Query}")

try:
    for i in range(1,Pages):
        MorePages = driver.find_element(By.XPATH, f'//*[@id="rld-{i}"]/a')
        MorePages.click()
except:
    pass

pageSource = driver.page_source
driver.quit()
if 'Make sure all words are spelled correctly.' in pageSource:
    exit('No Results Found.')

file = open('Results.txt', 'w')
urls = list(set(re.findall('</a></span><a href="(.*?)"',pageSource)))
for url in urls:
    print(url)
    file.write(url+'\n')

exit('Successfully Grabbed Urls.')
