# action :-  performing mouse and keyboard action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import  ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
driver.maximize_window()
sleep(2)
action = ActionChains(driver)

origin_ele = driver.find_element(By.ID , "column-a")
target_ele = driver.find_element(By.ID, "column-b")
action.drag_and_drop(origin_ele, target_ele).perform()
sleep(2)
