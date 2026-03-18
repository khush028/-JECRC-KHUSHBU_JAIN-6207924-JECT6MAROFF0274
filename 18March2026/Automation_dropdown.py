from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options= opts)
driver.get('https://testautomationpractice.blogspot.com/')
country_dropdown = driver.find_element(By.ID , 'country')
driver.maximize_window()  # so no overlapping

# select attribute to select the value by value , index , visible
dropdown = Select(country_dropdown)
dropdown.select_by_value("australia")
sleep(1)
dropdown.select_by_index(4)
sleep(2)
dropdown.select_by_visible_text('Japan')
sleep(2)
driver.quit()