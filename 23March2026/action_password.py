#click and hold 

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get(r"C:\PyCharm\23March2026\Password.html")

driver.maximize_window()
sleep(3)
action =ActionChains(driver)

driver.find_element(By.ID , "password").send_keys("khushbu@1234")
sleep(3)
show_pwd = driver.find_element(By.ID, "eyeBtn")
action.click_and_hold(show_pwd).perform()
sleep(3)
action.release()
