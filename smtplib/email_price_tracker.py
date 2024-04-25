from bs4 import BeautifulSoup
import requests
import smtplib
import time

EMAIL = "tumtiede123@gmail.com"
PASSWORD = "dlzfbgyplkxuidup"

URL = "https://uk.camelcamelcamel.com/product/B0779KYCVC?context=search"


def price_below():
    response = requests.get(URL,
                            headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                                     "Accept-Language": "en"})
    camel_page = response.text

    soup = BeautifulSoup(camel_page, 'html.parser')
    price = soup.find(class_="green").get_text()
    price_without_currency = float(price.split("£")[1])
    print(price_without_currency)
    if price_without_currency < 20.00:
        return True


while True:
    time.sleep(60)
    if price_below():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs="au_tiede@yahoo.com",
                                msg="Subject: Price change in Spinners!\n\n"
                                    "Figit Spinners are below 20 pounds! Get them while you can!")

    else:
        print("price is above target.")
