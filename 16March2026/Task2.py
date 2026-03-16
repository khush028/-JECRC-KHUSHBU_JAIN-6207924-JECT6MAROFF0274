# ## Task 2
#
# ### Radio Buttons
#
# Automate interaction with radio buttons `https://demoqa.com/radio-button`
#
# 1. Open the radio button page.
# 2. Print the **title** of the page.
# 3. Locate the **"Yes" radio button**.
# 4. Click the radio button using `click()`.
# 5. Capture and print the **result message** using `.text`.
# 6. Use `get_attribute()` to fetch attributes like:
#    - `class`
#    - `id`
# 7. Print the **current URL**.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/radio-button')
print("Title : " , driver.title )
radio_button = driver.find_element(By.XPATH , "//label[@for='yesRadio']")
radio_button.click()
print(" Result Message : - " , radio_button.text)
class_attr = radio_button.get_attribute("class")
id_attr = radio_button.get_attribute("for")
print("Class Attribute:", class_attr)
print("ID Attribute:", id_attr)
print("Current Url:-", driver.current_url)
