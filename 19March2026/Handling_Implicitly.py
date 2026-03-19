from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://abc.com/')
driver.maximize_window()

# implicitly wait =  it will work for all driver.element , it is global  , certain period , not found element the show no such element found
# find only the element  , if it's not visible on screen still it work because it only found in the drome structure

driver.implicitly_wait(5)
# ele = driver.find_element(By.XPATH , '(//a[@class = "AnchorLink"]/parent::li/descendant::span[3])[1]')
# print(ele.text)
image = driver.find_element(By.XPATH , '(//a[@class = "AnchorLink"]/parent::li/descendant::img)[1]')
print(image.get_attribute('src'))
driver.quit()