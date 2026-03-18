from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
male = driver.find_element(By.ID , 'male')
male.click()
#is_displayed = to know that male is present or display or not (give output in TRUE OR FALSE
print(male.is_displayed())
#is_enabled = is this selected or not return output in True or False
print(male.is_enabled())
days = driver.find_element(By.XPATH ,'//label[text() ="Monday"]/preceding-sibling::input')
days.click()
#is_selected = to check is it selected or not
print(days.is_selected())


