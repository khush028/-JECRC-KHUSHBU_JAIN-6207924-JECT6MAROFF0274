from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get(r"C:\PyCharm\20March2026\playlist.html")
driver.maximize_window()


multi_drop = driver.find_element(By.ID , "songs")
select = Select(multi_drop)

# if elif
if select.is_multiple:
    for i in select.options:
        if i.text.__contains__("Girl"):
            select.select_by_visible_text(i.text)
        elif i.text.__contains__("Love"):
            select.select_by_visible_text(i.text)

# assert
# if select.is_multiple:
#     for i in select.options:
#         assert "Girl" in i.text or "Love" in i.text
#         select.select_by_visible_text(i.text)


print([i.text for i in select.all_selected_options])
driver.find_element(By.XPATH , "//button[text() ='Add to Playlist']").click()
sleep(5)
driver.quit()





