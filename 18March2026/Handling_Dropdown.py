from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options= opts)
driver.get('https://www.lenskart.com/lenskart-air-la-e17269-c1-eyeglasses.html')
driver.maximize_window()
sleep(2)
# eye = driver.find_element(By.ID ,'lrd1')
# # print(eye.text)
# # assert 'EYEGLASSES' in eye.text, 'didnot find'
# assert 'EYEGLASSES' == eye.text, 'didnot find'
# # assert 'GLASSES' == eye.text, 'didnot find'
# print("success")

pincode = driver.find_element(By.XPATH , '//h4[@class = "sc-84016674-0 dbhRRC"]')
print(pincode.is_enabled())
sleep(2)
pincode.click()
sleep(2)
pincode1 = driver.find_element(By.XPATH , '//div[@class = "sc-a3b31f26-14 fDEfLM"]')
print(pincode1.is_enabled())

driver.quit()