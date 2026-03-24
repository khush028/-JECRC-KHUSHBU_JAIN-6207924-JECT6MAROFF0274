from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
sleep(3)
# to the bottom of the page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
sleep(4)
# to the origin of page
driver.execute_script("window.scrollTo(0,0);")
sleep(4)
# using scroll by
# scrolling down 500 px
driver.execute_script("window.scrollBy(0,500);")
sleep(2)
# scrolling up 200 px from 500 px
driver.execute_script("window.scrollBy(0,-200);")
sleep(2)
ele=driver.find_element(By.XPATH,'//img[contains (@alt,"Photo of a woman in a cherry-patterned sweater vest, white shirt, blue skirt, ")]')
driver.execute_script("arguments[0].scrollIntoView();",ele)
sleep(2)
click_ele=driver.find_element(By.XPATH,'(//div[text()="Join Pinterest"])[1]')
driver.execute_script("arguments[0].click();",click_ele)
sleep(4)