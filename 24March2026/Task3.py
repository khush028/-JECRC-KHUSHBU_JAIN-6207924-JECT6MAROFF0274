from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
driver.find_element(By.ID,"tabButton").click()
tab_count=driver.window_handles
# print(len(tab_count))
driver.switch_to.window(tab_count[-1])
heading=driver.find_element(By.ID,"sampleHeading")
assert "This is a sample page" == heading.text,"no text shown"
print("you have opened a new tab")
driver.close()
driver.switch_to.window(tab_count[0])
windowbtn=driver.find_element(By.ID,"windowButton")
windowbtn.click()
window_count=driver.window_handles
# print(len(window_count))
driver.switch_to.window(window_count[-1])
heading2=driver.find_element(By.ID,"sampleHeading")
assert "This is a sample page" == heading2.text,"no text shown"
print("you are now in new window")
driver.close()
driver.switch_to.window(window_count[0])
wait=WebDriverWait(driver,10)
new_window=wait.until(EC.visibility_of_element_located((By.ID,"messageWindowButton")))
new_window.click()
new_window_count=driver.window_handles
print(len(new_window_count))
driver.switch_to.window(new_window_count[-1])

# driver.maximize_window()
driver.close()
driver.switch_to.window(new_window_count[0])
driver.quit()