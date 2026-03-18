from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options= opts)
driver.get('https://www.lenskart.com/lenskart/')
driver.maximize_window()
sleep(2)
search_bar = driver.find_element(By.XPATH , "//input[@type = 'search']")
search_bar.send_keys('sunglasses' , Keys.ENTER)
sleep(2)
sort = driver.find_element(By.ID , 'sortByDropdown')
sorted1 = Select(sort)
# sorted1.select_by_index(4)
sorted1.select_by_index(1)
sleep(1)
inner_text = driver.find_element(By.XPATH , "(//div[@class = 'sc-bf32d8a7-0 gOVKHN'])[1]/descendant::p[@class = 'sc-23b7d3eb-2 dQrJBg'][1]")
inner_text1 = driver.find_element(By.XPATH , "(//div[@class = 'sc-bf32d8a7-0 gOVKHN'])[1]/descendant::p[@class = 'sc-23b7d3eb-2 dQrJBg'][2]")
print(inner_text.text)
print(inner_text1.text)
