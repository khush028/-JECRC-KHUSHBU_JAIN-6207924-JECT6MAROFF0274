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

# scroll to element
catto = driver.find_element(By.XPATH , '//div[@data-ganame = "Breed 5"]')
action.scroll_to_element(catto).perform()
sleep(2)

# scroll down = positive
# scroll up = negative
# scroll to = exact position

# scroll up
action.scroll_by_amount(0,-1500).perform()
sleep(5)

# mouse click = click(left)  ,  context(right) , double(double click) we use all this with action



