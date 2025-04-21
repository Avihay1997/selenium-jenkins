from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5000/")
time.sleep(1)
assert "Home" in driver.title

login_link = driver.find_element(By.LINK_TEXT, "Login")
login_link.click()
time.sleep(1)

username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys("admin")
password_input.send_keys("password")
password_input.send_keys(Keys.RETURN)
time.sleep(1)

assert "Home" in driver.page_source

driver.quit()
