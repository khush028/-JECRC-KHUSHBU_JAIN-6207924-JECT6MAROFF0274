from selenium import webdriver
opts = webdriver.FirefoxOptions()
opts.set_preference("detach" , True)
driver = webdriver.Firefox(options=opts)
driver.get("https://youtube.com/")
driver.maximize_window()
# driver.close()