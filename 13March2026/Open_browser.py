from selenium import webdriver
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--headless")  # run browser in background

driver = webdriver.Chrome(options=opts)

driver.get("https://www.myntra.com/")

sleep(10)

driver.maximize_window()

print(driver.title)

driver.quit()