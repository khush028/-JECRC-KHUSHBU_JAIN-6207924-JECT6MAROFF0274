# go to myntra
# hover over men or women
# choose a category then click on it
# scroll to a 4th or 5 th product
# use proper waits

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from unicodedata import category

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options= opts)
driver.get("https://myntra.com/")
driver.maximize_window()


wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

women = wait.until(EC.element_to_be_clickable((By.XPATH , '(//div[@class = "desktop-navLink"])[2]')))
action.move_to_element(women).perform()

category_fav = wait.until(EC.element_to_be_clickable((By.XPATH ,'//li[@data-reactid="189"]')))
action.move_to_element(category_fav).perform()

category_fav.click()

fav_kurta = driver.find_element(By.XPATH , '//li[@id="25234310"]')
action.scroll_to_element(fav_kurta).perform()


print(fav_kurta.text)



