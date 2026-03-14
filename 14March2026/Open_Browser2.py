from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
price = driver.find_element(By.XPATH , '//td[text()="Learn Java"]/following-sibling::td[3]')
print("JAVA found")
text2 = driver.find_element(By.XPATH ,'//td[text()="Amod"]/ancestor::tr/preceding-sibling::tr[4]/child::td[3]')
print("Selenium Found")
text4 = driver.find_element(By.XPATH,'//td[text()=300]/preceding-sibling::td[3]')
print("Learn Selenium , Lear JS found")
text5 = driver.find_element(By.XPATH,'//tbody[@id="rows"]/child::tr/child::td[1]')
print("All Browsers found ")

