print("----------LensKart Website Tester---------------------")

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options= opts)
driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(2)
search_bar = driver.find_element(By.ID,'search-page')
next_data = driver.find_element(By.ID,'__NEXT_DATA__')
footer_content = driver.find_element(By.ID ,'footerContent')
main_content = driver.find_element(By.ID ,'main-content')
head = driver.find_element(By.ID , 'header')
search = driver.find_element(By.CLASS_NAME,'search-page')
input_suffix = driver.find_element(By.CLASS_NAME,'aa-InputWrapperSuffix')
form = driver.find_element(By.CLASS_NAME,'aa-Form')
input_text = driver.find_element(By.CLASS_NAME,'aa-input-search-box')
button = driver.find_element(By.CLASS_NAME ,'aa-ClearButton')
# NAME
view=driver.find_element(By.NAME,"viewport")
bar=driver.find_element(By.NAME,"apple-mobile-web-app-status-bar-style")
head1=driver.find_element(By.NAME,"next-head-count")
twitter=driver.find_element(By.NAME,"twitter:image")
des=driver.find_element(By.NAME,"description")

#Tag Name
inputs = driver.find_elements(By.TAG_NAME, "input")
buttons = driver.find_elements(By.TAG_NAME, "button")
links = driver.find_elements(By.TAG_NAME, "a")
heading = driver.find_element(By.TAG_NAME, "h1")
para = driver.find_element(By.TAG_NAME, "p")

# print(search)
print("ID:-Search bar , next , footer Content ,  MAIN-CONTENT and  header are  found")
print("CLASS NAME : -search page found , input suffix found , form aa found , text search found and clear botton found")
print("NAME :- view found , bar found , head1 found , twitter found and des found")
print("TAG NAME :- inputs found , buttons found , links founds , heading found and para founds")
# print(search_bar)


