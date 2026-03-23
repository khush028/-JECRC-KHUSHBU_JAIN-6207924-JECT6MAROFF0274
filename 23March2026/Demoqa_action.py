# action :-  performing mouse and keyboard action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options= opts)
driver.get("https://demoqa.com/droppable")
driver.maximize_window()
sleep(2)
action = ActionChains(driver)

draggable_ele = driver.find_element(By.XPATH, '//div[@id="draggable"]')
droppable_ele = driver.find_element(By.XPATH, '//div[@id="droppable"]')
action.drag_and_drop(draggable_ele,droppable_ele).perform()
sleep(2)

text1 = driver.find_element(By.XPATH, '(//div[@id="droppable"]/child::p)[1]')
assert 'Dropped!' in text1.text , "not drag"
print("yes i'm dropped ")
