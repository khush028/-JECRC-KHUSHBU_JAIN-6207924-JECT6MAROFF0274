
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
sleep(3)
# it return current url address
parent_window=driver.current_window_handle
driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
sleep(3)
all_windows=driver.window_handles
print(len(all_windows))
driver.switch_to.window(all_windows[-1])
print(driver.current_window_handle)
# print(driver.find_element(By.CLASS_NAME,"example").text)
assert "New" in driver.find_element(By.CLASS_NAME,"example").text
print("done")
# instead of using indexing
driver.close()
driver.switch_to.window(parent_window)
print(driver.current_window_handle)