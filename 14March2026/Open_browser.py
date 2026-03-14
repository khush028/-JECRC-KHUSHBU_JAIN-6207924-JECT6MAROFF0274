from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
# driver.get('https://www.myntra.com/')
# sleep(3)
driver.get("https://www.amazon.in/")
sleep(3)
# driver.get("https://www.cricbuzz.com/")
# sleep(3)
# ancestor = find our parent one
text1 = driver.find_element(By.XPATH ,'//label[@for =  "twotabsearchtextbox"]/ancestor::div[@class="nav-search-field "]')
print("Ancestor Found")
# descendant : - find our child one

text2 = driver.find_element(By.XPATH ,'//div[@class = "nav-search-field "]/descendant::input[@type = "text"]')
print("Descendant Found")

#preceding : - to find the ancestor sibling

text3 = driver.find_element(By.XPATH,'//div[@class = "nav-fill"]/preceding-sibling::div')
print("Preceding Sibling Found")

# following-sibling : - your younger one sibling

text4 = driver.find_element(By.XPATH,'//div[@class = "nav-fill"]/following-sibling::div')
print("Following Sibling Found")

#Partial LInk text : -

text5 = driver.find_element(By.LINK_TEXT, "Join Prime")
print("Today's deal found")

# text6 = driver.find_element(By.PARTIAL_LINK_TEXT ,)