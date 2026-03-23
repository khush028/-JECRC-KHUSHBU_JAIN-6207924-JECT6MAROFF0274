from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("https://demoqa.com/droppable")

driver.maximize_window()
sleep(3)
action =ActionChains(driver)
wait=WebDriverWait(driver,10)

pp_btn=wait.until(EC.element_to_be_clickable((By.ID,"droppableExample-tab-preventPropogation")))
pp_btn.click()
drag=wait.until(EC.element_to_be_clickable((By.ID,'dragBox')))
outer_drop=wait.until(EC.visibility_of_element_located((By.XPATH,'(//div[@id="notGreedyDropBox"]/child::p)[1]')))
action.drag_and_drop(drag,outer_drop).perform()
inner_drop=wait.until(EC.visibility_of_element_located((By.ID,'notGreedyInnerDropBox')))
action.drag_and_drop(drag,inner_drop).perform()
outer_Drop2=wait.until(EC.visibility_of_element_located((By.XPATH,'(//div[@id="greedyDropBox"]/child::p)[1]')))
action.drag_and_drop(drag,outer_Drop2).perform()
action.scroll_to_element(outer_drop).perform()

# sleep(3)
inner_drop2=wait.until(EC.visibility_of_element_located((By.ID,'greedyDropBoxInner')))
action.drag_and_drop(drag,inner_drop2).perform()
sleep(4)