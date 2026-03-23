# keyboard Action

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import  ActionChains

from time import sleep

driver = webdriver.Chrome()
driver.get("https://supertails.com/")
driver.maximize_window()
sleep(2)
action = ActionChains(driver)

action.send_keys(Keys.PAGE_DOWN).perform()
sleep(3)

action.send_keys(Keys.PAGE_UP).perform()
sleep(3)

action.key_down(Keys.CONTROL).send_keys('a').perform()   # this will control the keys like ctrl c , ctrl a  etc
sleep(3)

action.key_up(Keys.CONTROL).perform()
sleep(3)