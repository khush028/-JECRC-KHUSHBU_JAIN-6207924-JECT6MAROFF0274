from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://demo.mobiscroll.com/select/multiple-select/')
driver.maximize_window()

multi_drop = driver.find_element(By.XPATH , '//select[@id = "multiple-select-select"]')
multi_select = Select(multi_drop)

if multi_select.is_multiple():
    multi_select.select_by_index(3)
    multi_select.select_by_value("Sports & Outdoors")
    multi_select.select_by_visible_text("Movies, Music & Games")


sleep(5)

multi_select.deselect_by_index(1)
multi_select.deselect_by_value("Sports & Outdoors")
multi_select.deselect_all()
print(multi_select.first_selected_option)
print(multi_select.all_selected_options)

driver.quit()
