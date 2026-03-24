from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
sleep(3)
# opening a website in new window
driver.switch_to.new_window('window')
driver.get("https://www.cricbuzz.com/")
sleep(4)
# opening window in new tab
driver.switch_to.new_window('tab')
driver.get("https://www.cricbuzz.com/")
sleep(4)
driver.switch_to.new_window("tab")
driver.get("https://www.linkedin.com/")
