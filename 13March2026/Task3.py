from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

# 1. Navigate to Amazon
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)

# 2. Search bar using ID with CSS Selector
search = driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
print("Search bar found")

# 3. Amazon logo using CSS Selector
logo = driver.find_element(By.CSS_SELECTOR, "#nav-logo-sprites")
print("Logo found")

# 4. Cart link/icon using CSS Selector
cart = driver.find_element(By.CSS_SELECTOR, "#nav-cart")
print("Cart found")

# 5. Sign in link using descendant selector (space)
signin = driver.find_element(By.CSS_SELECTOR, "#nav-tools a")
print("Sign in found")

# 6. Category links under navigation bar
categories = driver.find_elements(By.CSS_SELECTOR, "#nav-xshop a")
print("Total category links:", len(categories))