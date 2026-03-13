print("-------------Cricbuzz-----------")
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opts)
driver.get("https://www.cricbuzz.com")
driver.maximize_window()
sleep(3)

## Locator
# id :- ID locator finds an element using its unique id attribute in HTML.
banner = driver.find_element(By.ID, "smartifai_banner")
print("ID :- banner FOUND")

#CLASS_NAME : - CLASS_NAME locator identifies web elements by their class attribute.
wrap = driver.find_element(By.CLASS_NAME ,'page-wrapper')
print("CLASS_NAME :- wrapper found")

#NAME :- NAME locator is used to find an element using its name attribute in HTML.
element = driver.find_element(By.NAME, "twitter:card")
print("NAME : - Twitter Card Found")

#TAG_NAME :- TAG_NAME locator identifies elements by their HTML tag such as input, div, a, p, h1.
links = driver.find_elements(By.TAG_NAME, "a")
print("Anchor Tag :-" , len(links))
divs = driver.find_elements(By.TAG_NAME, "div")
print("Div Tag :-" ,len(divs))
inputs = driver.find_elements(By.TAG_NAME, "input")
print("Inputs Tags :-",len(inputs))
para = driver.find_elements(By.TAG_NAME, "p")
print("Paragraph Tag :- ",len(para))
heading = driver.find_elements(By.TAG_NAME, "h1")
print("Heading tag:- ", len(heading))

#CSS_SELECTOR :-CSS_SELECTOR locator is used to find elements using CSS rules like id, class, tag, attribute, and combinations.
id1 = driver.find_element(By.CSS_SELECTOR, "#smartifai_banner")
# class1 = driver.find_element(By.CSS_SELECTOR, ".cb-hm-mnu-itm")
# Tag_Class = driver.find_element(By.CSS_SELECTOR, "a.cb-hm-mnu-itm")
Tag_Id = driver.find_element(By.CSS_SELECTOR, "div#smartifai_banner")
Attribute = driver.find_element(By.CSS_SELECTOR, "a[href='/cricket-news']")
Contains = driver.find_element(By.CSS_SELECTOR, "a[href*='news']")
Start = driver.find_element(By.CSS_SELECTOR, "a[href^='/cricket']")
Ends = driver.find_element(By.CSS_SELECTOR, "a[href$='news']")
print("Css Selector Found")

#XPATH : - XPath is a locator used to find elements by navigating through HTML structure using tags, attributes, and text.

Xpath1 = driver.find_element(By.XPATH, "//div[@id='smartifai_banner']")
text = driver.find_element(By.XPATH, "//a[text()='Live Scores']")
print("Xpath , text()  found")