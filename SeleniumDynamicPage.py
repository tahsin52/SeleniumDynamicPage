from selenium import webdriver
import random
from selenium.webdriver.support.ui import Select
import time
 
browser = webdriver.Chrome()
 
# Dinamik Son Sayfayı Alma !!!
pageIDs = []
url0 = "https://eksisozluk.com/mustafa-kemal-ataturk--34712"
browser.get(url0)
time.sleep(3)
select = Select(browser.find_element_by_xpath("//*[@id='topic']/div[1]/div[2]/select"))
options = select.options
for opt in options:
    value = opt.get_attribute('value')
    pageIDs.append(int(value))
maxPageID = max(pageIDs)
# Dinamik Son Sayfayı Alma Bitti !!!
 
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
 
pageCount = 1
entries = []
entryCount = 1
 
while pageCount <= 10:
    randomPage = random.randint(1, maxPageID)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    elements = browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(1)
    pageCount += 1
 
for entry in entries:
    print(str(entryCount) + " ******************************")
    print(entry)
    entryCount += 1
 
browser.close()
