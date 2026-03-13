from selenium import webdriver
opts = webdriver.EdgeOptions()
opts.add_experimental_option("detach" , True)
driver = webdriver.Edge(options=opts)
driver.get("https://youtube.com/")
driver.maximize_window()
# driver.close()