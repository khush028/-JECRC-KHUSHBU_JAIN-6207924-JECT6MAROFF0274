from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options= opts)
driver.get('https://the-internet.herokuapp.com/upload')
driver.maximize_window()
sleep(2)

choose_file = driver.find_element(By.ID ,'file-upload')
choose_file.send_keys(r"C:\Users\hp\Downloads\AI ML Intern.pdf")

submit_btn = driver.find_element(By.ID , 'file-submit')
submit_btn.click()
print("File Uploaded")


