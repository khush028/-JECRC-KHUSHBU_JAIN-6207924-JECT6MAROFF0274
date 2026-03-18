from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options= opts)
driver.get('https://www.myntra.com/')
driver.maximize_window()
sleep(2)
beauty = driver.find_element(By.XPATH ,'//a[@data-group ="beauty"]')
assert 'BEAUTY' in beauty.text, 'didnot find'
print("Beauty Find")
driver.quit()


