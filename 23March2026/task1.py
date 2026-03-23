# fav website , scroll to fav photo ( for loop 5 times) , sroll up (5 times)

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("https://www.vogue.com/")

driver.maximize_window()

action =ActionChains(driver)

fav_img = driver.find_element(By.XPATH,'(//div[@class = "aspect-ratio--overlay-container"])[71]')
action.scroll_to_element(fav_img).perform()
sleep(3)

for i in range(0,6):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(1)

sleep(5)
driver.quit()