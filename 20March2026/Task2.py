from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

## for favourite artist all song
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get(r"C:\PyCharm\20March2026\playlist.html")
driver.maximize_window()
multi_drop1 = driver.find_element(By.ID, 'songs')
select1 = Select(multi_drop1)

if select1.is_multiple:
    fav_artist = driver.find_elements(By.XPATH, '//select[@id ="songs"]/child::optgroup[4]/child::option')
    for i in fav_artist:
        select1.select_by_visible_text(i.text)

print([i.text for i in select.all_selected_options])
driver.find_element(By.XPATH, "//button[text() ='Add to Playlist']").click()
sleep(5)
driver.quit()