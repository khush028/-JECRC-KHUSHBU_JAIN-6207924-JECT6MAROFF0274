from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep
from streamlit.components.v1 import iframe
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://codepen.io/gdw96/pen/jOypoYL")
driver.maximize_window()
wait=WebDriverWait(driver,10)
frame=driver.find_element(By.ID,"result")
driver.switch_to.frame(frame)
sleep(1)
user=wait.until(EC.presence_of_element_located((By.ID,"username")))

user.clear()
user.send_keys("kanika")
sleep(3)
password=wait.until(EC.visibility_of_element_located((By.ID,"password")))
password.clear()
password.send_keys("123455")
show_pass=wait.until(EC.visibility_of_element_located((By.ID,"showPsswd")))
show_pass.click()
btn=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@class="submit"]')))
btn.click()
sleep(5)
driver.back()
sleep(10)
frame=driver.find_element(By.ID,"result")
driver.switch_to.frame(frame)
register=driver.find_element(By.TAG_NAME,"h1")

assert "Registration" == register.text
print("Program Successfully")
driver.quit()