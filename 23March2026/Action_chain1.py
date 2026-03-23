# action :-  performing mouse and keyboard action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import  ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://supertails.com/")
driver.maximize_window()
sleep(2)
action = ActionChains(driver)

doggo = driver.find_element(By.XPATH , '(//span[contains(text(),"Dogs")])[1]')
action.move_to_element(doggo).perform()
sleep(2)