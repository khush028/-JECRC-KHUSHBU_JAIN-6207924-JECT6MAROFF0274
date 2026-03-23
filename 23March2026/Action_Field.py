from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome()
driver.get(r"C:\PyCharm\23March2026\Address.html")
driver.maximize_window()
sleep(2)
action = ActionChains(driver)


present_address = driver.find_element(By.ID , "presentAddress")
permanent_Address = driver.find_element(By.ID , "permanentAddress")
present_address.send_keys("Jaipur Rajasthan " , Keys.ENTER)

sleep(2)
present_address.click()

action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
sleep(2)

action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

permanent_Address.click()
sleep(2)

action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
sleep(2)
