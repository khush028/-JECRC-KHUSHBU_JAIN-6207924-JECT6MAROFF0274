# ## Task 2
#
# ### Registration Form
#
#
# 1. Go to: https://demoqa.com/automation-practice-form
# 2. Handle every element in that form except the calendar
# `Note: Give fake names and emails`
# 3. Click on submit button

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(3)
driver.find_element(By.ID, "firstName").send_keys("Bhav")
driver.find_element(By.ID, "lastName").send_keys("Jain")
driver.find_element(By.ID, "userEmail").send_keys("Bhavjaink@gamil.com")
driver.find_element(By.XPATH, "//label[@for='gender-radio-2']").click()
driver.find_element(By.ID, "userNumber").send_keys("1234567890")
subjects = driver.find_element(By.ID, "subjectsInput")
subjects.send_keys("Science")
subjects.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, "//input[@id='hobbies-checkbox-1']").click()
driver.find_element(By.XPATH, "//input[@id='hobbies-checkbox-2']").click()
driver.find_element(By.ID, "uploadPicture").send_keys(r"C:\Users\hp\OneDrive\Pictures\khushbu photo.jpg")
driver.find_element(By.ID, "currentAddress").send_keys("Jaipur, Rajasthan")
driver.find_element(By.ID, "react-select-3-input").send_keys("NCR")
driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.ENTER)
driver.find_element(By.ID, "react-select-4-input").send_keys("Delhi")
driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.ENTER)
driver.find_element(By.ID, "submit").click()
time.sleep(3)
print("Form Submitted Successfully")
driver.quit()