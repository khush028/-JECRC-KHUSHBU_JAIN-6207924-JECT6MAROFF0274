# An iframe (Inline Frame) is an HTML element used to embed another webpage inside a webpage.
# An iframe allows you to display one HTML page inside another HTML page.
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from streamlit.components.v1 import iframe

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
sleep(3)
# single iframe
'''
frame=driver.find_element(By.ID,"singleframe")
driver.switch_to.frame(frame)
sleep(2)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys('123')
sleep(5)
'''
# nested iframe
driver.find_element(By.XPATH,'//a[text()="Iframe with in an Iframe"]').click()
nested_iframe=driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(nested_iframe)
inner_iframe=driver.find_element(By.XPATH,'//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inner_iframe)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys('123')
sleep(5)
driver.switch_to.parent_frame() #switches to parent frame
driver.switch_to.default_content() #switches to default page
