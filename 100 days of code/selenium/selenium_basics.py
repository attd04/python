from selenium import webdriver
from selenium.webdriver.common.by import By

# keep tab open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.ebay.com/itm/196141131222?hash=item2daaec25d6:g:PVsAAOSwsYRleDul&amdata=enc%3AAQAIAAAA0D4Xuv8XVBkeQLpOT9FJ92oW%2BDAs4gzrW5E5nqePL%2FaJrSl%2BD98vKlLQvlijX6VNvHBjZ6TDI1D9XDMvHF5qJvavC%2B153Pmg96xA95LpW0aNUnTrHcY7%2FArwMt2QxjUvSjI5I1Yu4pqXzbLu8tVDHJFrx3nEzIjj1KurmAwBJ5zZpQ7ggPag5YE6csMnC2On20rwHEC2aSB%2Bv%2F%2Fk5eoJGXGDCjK7wpwg7e4E1W5E9uahuBJhhOyuiA%2F89D875C3jAwiw4gkRYahP3K4IG4aDi4U%3D%7Ctkp%3ABFBM5tSOopBj")

price = driver.find_element(By.CLASS_NAME, value="x-bin-price__content")
print(f"The price is {price.text}.")

# or use xpath:
# title = driver.find_element(By.XPATH, value'"//*[@id="mainContent"]/div/div[1]/h1/span")
# print(title.size)

# driver.close()
# closes most recent page

driver.quit()
# closes entire browser
