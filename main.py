import requests
import smtplib
import os
from bs4 import BeautifulSoup

MY_EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["PASSWORD"]
TARGET_EMAIL = os.environ["TARGET_EMAIL"]
APP_PASSWORD = os.environ["APP_PASSWORD"]

TARGET_PRICE = 90.00

amazon_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.6"
}

response = requests.get(url=amazon_url,headers=header)

soup = BeautifulSoup(response.content,"html.parser")
current_price = float(soup.find(class_="a-offscreen").getText().strip("$"))

message = "Hi there"

if current_price<=TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TARGET_EMAIL,
            msg=message.encode("utf-8")
        )