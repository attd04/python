from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeckf9pQzbVKk3YjFRZYtT6UZn95waZs-3i20p7o5T6s8TwPQ/viewform?usp=sf_link"
zillow_url = "https://appbrewery.github.io/Zillow-Clone/"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(zillow_url, header)
zillow_page = response.text

soup = BeautifulSoup(zillow_page, 'html.parser')

# get links
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]

# get addresses
all_addresses_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace("|", "").strip() for address in all_addresses_elements]

# get prices
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().strip("+mobd/")[:6] for price in all_price_elements]



# selenium to fill in google doc
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(google_form_url)

for num in range(len(all_prices)):
    print(num)
    address = driver.find_element(By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(all_addresses[num])

    price = driver.find_element(By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(all_prices[num])

    link = driver.find_element(By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(all_links[num])

    submit = driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()

    again = driver.find_element(By.XPATH,
                                value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    if num != len(all_prices):
        again.click()

driver.quit()
