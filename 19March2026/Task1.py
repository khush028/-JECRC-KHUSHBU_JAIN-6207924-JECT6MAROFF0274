# image banner of all 8
# not use implicit and explicit together because it overlap in it
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://abc.com/')
driver.maximize_window()
wait_obj = WebDriverWait(driver,5)

banner_images = wait_obj.until(EC.presence_of_all_elements_located((By.XPATH , '(//div[@id ="hero-items"]//child::div[@class = "Image__Wrapper aspect-ratio--child"][1])/descendant::img')))
for images in banner_images:
    print(images.get_attribute("src"))

driver.quit()