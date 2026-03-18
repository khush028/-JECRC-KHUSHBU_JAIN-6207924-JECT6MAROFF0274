# ## Task 1
#
# ### Link Text & Partial Link Text
#
#
# 1. Go to https://the-internet.herokuapp.com/
# 2. Find the "Checkboxes" link using LINK_TEXT
# 3. Find the "Drag and Drop" link using PARTIAL_LINK_TEXT
# 4. Find how many <li> (list item) elements are on the page using find_elements and TAG_NAME. Print the count.
# 5. Navigate to https://the-internet.herokuapp.com/tables
# 6. Write an XPath to find the "Web Site" (td) for the person with email "jdoe@hotmail.com" in table 1 (Hint: Use text() and ancestor/following sibling or preceding-sibling).
# 7. Write an XPath to find the Delete link (a) for the person with Last Name "Bach" in table 1.
# 8. Write an XPath to find the second table `(<table>)` on the page using indexing.
# 9. Write an XPath to find the cell containing "$100.00" in table 2. Find its parent <tr> element.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)
checkbox_link = driver.find_element(By.LINK_TEXT, "Checkboxes")
print("Checkboxes link found")
drag_drop_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Drag")
print("Drag and Drop link found")
list_items = driver.find_elements(By.TAG_NAME, "li")
print("Total <li> elements:", len(list_items))
driver.get("https://the-internet.herokuapp.com/tables")
time.sleep(2)
website = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='jdoe@hotmail.com']/following-sibling::td[2]")
print("Website (jdoe):", website.text)
delete_link = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='Bach']/following-sibling::td//a[text()='delete']")
print("Delete link for Bach found")
second_table = driver.find_element(By.XPATH, "(//table)[2]")
print("Second table located")
cell_100 = driver.find_element(By.XPATH, "//table[@id='table2']//td[text()='$100.00']")
parent_row = cell_100.find_element(By.XPATH, "./parent::tr")
print("Cell value:", cell_100.text)
print("Parent row text:", parent_row.text)
driver.quit()
