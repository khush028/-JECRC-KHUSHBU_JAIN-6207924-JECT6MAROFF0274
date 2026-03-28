from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://demoqa.com/alerts")
driver.maximize_window()

btn1=driver.find_element(By.ID,"alertButton")
btn1.click()
alert_btn1=driver.switch_to.alert
alert_btn1.accept()


wait=WebDriverWait(driver,10)
alert_btn=wait.until(EC.element_to_be_clickable((By.ID,"timerAlertButton")))
alert_btn.click()
simple_alert=wait.until(EC.alert_is_present())
simple_alert.accept()

confirm_btn=driver.find_element(By.ID,"confirmButton")
confirm_btn.click()
alert_confirm_btn=driver.switch_to.alert
alert_confirm_btn.accept()
text_cnfm=driver.find_element(By.ID,"confirmResult")
assert "You selected " in text_cnfm.text,"btn not clicked"
print("btn is clicked an on clicking u are getting:",text_cnfm.text)

wait.until(EC.element_to_be_clickable((By.ID,"promtButton"))).click()
alert_text_btn=driver.switch_to.alert
alert_text_btn.send_keys("Kanika")
alert_text_btn.accept()
text2=driver.find_element(By.ID,"promptResult")
assert "You entered " in text2.text,"btn not clicked"
print(f"The text is {text2.text}")
driver.quit()