from itertools import product

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
# print(driver.title)
# print(driver.current_url)
assert "https://www.amazon.in/" ==driver.current_url,"not matched"
print("verified")
wait=WebDriverWait(driver,10)

wait.until(EC.presence_of_element_located((By.ID,"twotabsearchtextbox"))).send_keys("Headphones")
wait.until(EC.element_to_be_clickable((By.ID,"nav-search-submit-button"))).click()
range=wait.until(EC.element_to_be_clickable((By.XPATH,'//li[@id="p_36/dynamic-picker-2"]/descendant::span[@class="a-size-base a-color-base"]')))
range.click()
# print(range.text)
brand=wait.until(EC.visibility_of_element_located((By.XPATH,'//li[@id="p_123/214020"]/descendant::label')))
brand.click()

headphone=wait.until(EC.element_to_be_clickable((By.XPATH,'(//span[@class="rush-component"]/descendant::img[@class="s-image"])[3]')))
headphone.click()
window_count=driver.window_handles
driver.switch_to.window(window_count[-1])
product=wait.until(EC.presence_of_element_located((By.XPATH,'//span[@id="productTitle"]')))
product_name=product.text
print(product_name)
price=wait.until(EC.presence_of_element_located((By.XPATH,'(//span[@class="a-price-whole"])[6]')))
assert "Boat Rockerz 371, 40mm Drivers, 50hrs Battery, 60ms Low Latency, ENx Tech, BT v5.4, Foldable Cups, Voice Assistant, Bluetooth Headphone" in product.text,"not matched"
print("product found")
assert "999"==price.text,"not matched"
print("price matched")
add_cart=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@id="add-to-cart-button"]')))
add_cart.click()
wait.until(EC.element_to_be_clickable((By.XPATH,'//span[@class="a-button-inner"]/input[@aria-labelledby="attachSiNoCoverage-announce"]'))).click()
cart=wait.until(EC.presence_of_element_located((By.XPATH,'//span[@id="sw-gtc"]/descendant::a[@class="a-button-text"]')))
cart.click()
cart_title=wait.until(EC.visibility_of_element_located((By.XPATH,'//span[@class="a-truncate-cut"]')))

assert cart_title.text in product_name,"not same product"
print("same product added")



# better structure
# easy keywords to learn
# easy to maintain
# reusabilty
# easy to scale
# less codeability
# info is for inforamtion by default it consider log as info
