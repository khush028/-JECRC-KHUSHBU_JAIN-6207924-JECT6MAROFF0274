import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
# it joins current directory and the folder u want
folder=os.path.join(os.getcwd(),"screenshots")
os.makedirs(folder,exist_ok=True)
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://in.pinterest.com/")
driver.maximize_window()
sleep(2)
# Two methods to take the ss

driver.save_screenshot(f"{folder}/full_page.png")
sleep(4)
action=ActionChains(driver)
ele=driver.find_element(By.XPATH,'//img[contains (@alt,"Photo of a woman in a cherry-patterned sweater vest, white shirt, blue skirt, ")]')
action.scroll_to_element(ele).perform()
sleep(1)
ele.screenshot(f"{folder}/cherry_red.png")
driver.exit()