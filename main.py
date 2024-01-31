import requests
from datetime import datetime
import smtplib

MY_LAT = 38.026169
MY_LONG = -4.381870
MY_MAIL = "arathoriiicsr2@gmail.com"
PASSWORD = "gzqwgfsxaeiasvyf"


def on_point():
    response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response1.raise_for_status()
    data1 = response1.json()

    iss_latitude = float(data1["iss_position"]["latitude"])
    iss_longitude = float(data1["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        return False


def is_night():
    if sunrise >= hour >= sunset:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)
print(sunset)

time_now = datetime.utcnow()
hour = time_now.hour


if is_night() and on_point():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_MAIL,
            to_addrs=MY_MAIL,
            msg="Subject:EEEYY, look at the sky! ISS is near!!\n\nTime to set up!"
        )
