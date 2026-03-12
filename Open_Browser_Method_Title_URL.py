from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://github.com/khush028/-JECRC-KHUSHBU_JAIN-6207924-JECT6MAROFF0274")
print("Name :",driver.name)
print("Title:", driver.title)
print("URL:", driver.current_url)
driver.quit()