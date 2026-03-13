from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opts)
driver.get("https://youtube.com/")
driver.maximize_window()
# driver.close() # only present window will be close
driver.quit() # entire window will be quit
