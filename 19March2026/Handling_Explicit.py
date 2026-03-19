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

# synchronous error we use this because our ui not support our speed
# explicit - for explicit import webdriverwait and expected condition it is  confined it will output
# because condition will be different
# timeout error exception - wait only the time you give
# it's not global , its particular element
# condition :- dom , button not working , not clickable ,
# poll_frequency =  how much time it will go back to 10 sec
wait_obj = WebDriverWait(driver ,10)
Loading_Circles = wait_obj.until(EC.invisibility_of_element_located((By.ID , 'preloader-animated_svg__circle3')))
title_abc = driver.find_element(By.XPATH , '//span[text() ="ABC SHOWS, SPECIALS & MORE"]')
assert 'SPECIALS' in title_abc.text , 'the text not present'
print("Working Fine")
# Loading_Circles.click()
driver.quit()
