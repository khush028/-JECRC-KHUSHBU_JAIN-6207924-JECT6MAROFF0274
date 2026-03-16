from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
gender = input("Enter your gender:")
name = driver.find_element(By.ID ,'name')
# clear key = it will clear previous one
name.clear()
# send_keys = it will send the input by us
name.send_keys("khushbu")
email = driver.find_element(By.XPATH , "//input[@placeholder = 'Enter EMail']")
email.send_keys("khushbujaink7568@gmail.com")
#radio button selection
# gender = driver.find_element(By.ID , 'female').click()
# if condition  access gender
if gender == "male":
    driver.find_element(By.ID , 'male').click()
else:
    driver.find_element(By.ID , "female").click()
# click and unclick days
days = driver.find_elements(By.XPATH ,'//div[@class ="form-check form-check-inline"]/input[@type="checkbox"]' )
for i in days:
    i.click()
    sleep(1)
    # i.click()
    print(i.get_attribute("value"))
# for j in days:
#     j.click()
#     sleep(1)
for j in days[::-1]:
    j.click()
    sleep(1)
# days = driver.find_element(By.XPATH ,'//label[text() ="Monday"]/preceding-sibling::input').click()
# sleep(5)
# text = to know what the text return
day = driver.find_element(By.XPATH ,'//input[@id = "monday"]/following-sibling::label')
print(day.text)
print(name.get_attribute('placeholder'))
print(email.get_attribute("value"))


