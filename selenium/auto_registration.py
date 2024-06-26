from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Autumn")

l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("T")

email = driver.find_element(By.NAME, value="email")
email.send_keys("au_tiede@yahoo.com")

submit = driver.find_element(By.CSS_SELECTOR, value=".form-signin button")
submit.click()

driver.quit()
