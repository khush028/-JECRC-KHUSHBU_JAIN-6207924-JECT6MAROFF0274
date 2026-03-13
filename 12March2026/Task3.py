from selenium import webdriver
import time
browsers = [
     webdriver.Chrome,
     webdriver.Edge,
     webdriver.Firefox
]

for browser in browsers :
    driver = browser()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    driver.back()
    driver.forward()
    driver.refresh()
    # driver.minimize_window()
    print("Name : " , driver.name)
    print("Title :" , driver.title)
    print("URL :" , driver.current_url)
    time.sleep(5)
    driver.quit()