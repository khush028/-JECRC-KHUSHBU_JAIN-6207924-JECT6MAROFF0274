from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.lenskart.com/')
driver.maximize_window()
searchpage = driver.find_element(By.XPATH , "//input[@placeholder = 'What are you looking for?']")
# search_field = driver.find_element(By.XPATH ,'//div[@class="aa-GradientBottom"]')
searchpage.clear()
# Keys : - to do automated search
searchpage.send_keys("lenses" , Keys.ENTER)
# search_field.click()
print(searchpage.get_attribute("placeholder"))
print(searchpage.get_attribute("value"))