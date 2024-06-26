import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 54.689461
MY_LONG = 25.279860
EMAIL = "tumtiede123@gmail.com"
PASSWORD = "dlzfbgyplkxuidup"


def is_iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    # tells us which http error is coming up

    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


# finding sunrise / set times
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])

time_now = int(datetime.now().hour)

while True:
    time.sleep(60)
    if is_iss_above():
        if time_now >= sunset or time_now <= sunrise :
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL,
                                    to_addrs="au_tiede@yahoo.com",
                                    msg="Subject: ISS is visable now!\n\n"
                                        "The ISS is flying above you right now! Look up!")
        else:
            print("It is not dark yet.")
