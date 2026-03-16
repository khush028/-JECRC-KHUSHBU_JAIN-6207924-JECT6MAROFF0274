from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from unicodedata import category

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.flipkart.com/')
driver.maximize_window()
search_page = driver.find_element(By.XPATH, "//form[@class ='lilxh_ header-form-search']/descendant::input[@title='Search for Products, Brands and More']")
search_page.click()
search_page.send_keys("phone" , Keys.ENTER)
# sleep(2)
brand = driver.find_element(By.XPATH ,'//div[@class="buvtMR"]')
brand.click()
print(brand.text)
img = driver.find_element(By.XPATH ,'(//div[@class="lWX0_T"]/img[@class="UCc1lI"])[1]')
print(img.get_attribute('src'))
# Rating.click()
# Rating.send_keys()
# driver.quit()

