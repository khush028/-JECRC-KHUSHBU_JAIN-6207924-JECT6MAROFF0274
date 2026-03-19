# TAsk 3
# 1. navigate to amazon
# 2. search a product through send_keys
# BUT dont click on search or keys.enter
# 3. Wait for the suggestions to appear
# 4. Click on 4th suggestion
# 5. Click on Sort By and click on newest
# 6. Click on free shipping check box
# 7. wait for first product and return me the name=price
# (without using inner text)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in/')
driver.maximize_window()

wait_obj = WebDriverWait(driver ,5)

#2
input1 = wait_obj.until(EC.element_to_be_clickable((By.XPATH , "//input[@id ='twotabsearchtextbox']")))
input1.send_keys("shoes")

#3,4
suggestion = wait_obj.until(EC.element_to_be_clickable((By.XPATH,'//div[@class="left-pane-results-container"]/child::div[4]')))
suggestion.click()

#5
# click sort dropdown first
sort_dropdown = wait_obj.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='a-dropdown-prompt']")))
sort_dropdown.click()

# click newest arrivals
newest = wait_obj.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='s-result-sort-select_4']")))
newest.click()

# free shipping
shipping1 = wait_obj.until(EC.element_to_be_clickable((By.XPATH , '//span[@data-csa-c-content-id= "p_n_free_shipping_eligible/205563695031"]')))
shipping1.click()

#first name and price
name=wait_obj.until(EC.presence_of_element_located((By.XPATH,'(//span[@class="a-size-base-plus a-color-base"])[1]')))
price=wait_obj.until(EC.presence_of_element_located((By.XPATH,'(//span[@class="a-price"])[1]')))
print(f"name {name.text} price {price.text}")