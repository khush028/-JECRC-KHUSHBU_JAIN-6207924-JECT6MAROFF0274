from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
# opts.add_argument("--headless")   # run browser in background

driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")   # correct URL
driver.maximize_window()
sleep(2)
# name = driver.find_element(By.ID,'name')
# phone_no = driver.find_element(By.ID,'phone')
# nav_bar = driver.find_element(By.NAME ,'Navbar')
# # radio_button = driver.find_element(By.Class_Name,'from-check-input')
# radio_button = driver.find_elements(By.CLASS_NAME,'form-check-input')
# print(radio_button)
# print(len(radio_button))
# inp = driver.find_elements(By.TAG_NAME ,'input')
# print(len(inp))
# # print(name)
# print('name and phone textfield found')
# print('Navigation bar found')
# name1 = driver.find_element(By.CSS_SELECTOR,'select[id="animals"]')
# name2 = driver.find_element(By.CSS_SELECTOR,'#animals')
# anchor = driver.find_element(By.CSS_SELECTOR,'a[href*="testautomationpractice"]')
# print('a',anchor)
# anchor1 = driver.find_element(By.CSS_SELECTOR,'a[href^="https://"]')
# print('a',anchor1)
# anchor2 = driver.find_element(By.CSS_SELECTOR,'a[href$=".com/"]')
# print('a',anchor2)
# # print(name1)
# driver.quit()

# NoSuchElementExecptionn ;- when element not found or we write wrong spelling

#xpath -> t's very efficient and we can traverese back also any find element lower compare to other css selector
# difficult to understand also , / absolute xpath , // relative xpath
#perferred to use relative path
# //input[@id='name']

name3 = driver.find_element(By.XPATH , "(//input[@class='form-control'])[1]")
print(name3.get_attribute("id"))
name3 = driver.find_element(By.XPATH , "(//input[@class='form-control'])[2]")
print(name3.get_attribute("id"))
name3 = driver.find_element(By.XPATH , "(//input[@class='form-control'])[3]")
print(name3.get_attribute("id"))


# inner text in x path -> //a[text()="Home"]

name4 = driver.find_element(By.XPATH , "//a[text()='Home']")
print(name4.text)
name5 = driver.find_element(By.XPATH , "//h1[text()=' Automation']")
print(name5)

