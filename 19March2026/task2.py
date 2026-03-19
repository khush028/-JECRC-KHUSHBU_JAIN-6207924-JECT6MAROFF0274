from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://qavbox.github.io/demo/signup/')
driver.maximize_window()

wait_obj = WebDriverWait(driver ,5)

name = wait_obj.until(EC.presence_of_element_located((By.XPATH ,'//input[@id ="username"]')))
name.send_keys("Khushbu")

email = wait_obj.until(EC.presence_of_element_located((By.XPATH ,'//input[@id = "email"]')))
email.send_keys("khushbujaink7568@gamil.com")

telephone = wait_obj.until(EC.presence_of_element_located((By.XPATH ,'//input[@id = "tel"]')))
telephone.send_keys("9084687278")

# fax_no = wait_obj.until(EC.presence_of_element_located((By.XPATH ,'//input[@id = "fax"]')))
# fax_no.send_keys("305203")

profile = wait_obj.until(EC.presence_of_element_located((By.XPATH ,'//input[@multiple = "multiple"]')))
profile.send_keys(r"C:\Users\hp\OneDrive\Pictures\personal\photo.jpg")

gender = wait_obj.until(EC.presence_of_element_located((By.XPATH , '//option[@value ="female"]')))
gender.click()

experience = wait_obj.until(EC.presence_of_element_located((By.XPATH , '//input[@name = "experience"][1]')))
experience.click()

skills1 = wait_obj.until(EC.presence_of_element_located((By.XPATH ,'//input[@id = "ip"][1]')))
skills1.click()

skills2 = wait_obj.until(EC.presence_of_element_located((By.XPATH ,'//input[@id = "ip"][2]')))
skills2.click()

skills3 = wait_obj.until(EC.presence_of_element_located((By.XPATH ,'//input[@id = "ip"][3]')))
skills3.click()

tools = wait_obj.until(EC.presence_of_element_located((By.XPATH ,'//select[@id = "tools"]//child::option[1]')))
tools.click()

submit_btn = wait_obj.until(EC.presence_of_element_located((By.XPATH ,'//input[@id ="submit"]')))
submit_btn.click()
