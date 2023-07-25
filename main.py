import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.com/CUSIMAX-Smokeless-Extractor-Technology-Dishwasher-Safe/dp/B088T8B3Z2/ref=sr_1_3?keywords=smokeless%2Bindoor%2Bgrill%2Bkorean%2Bbbq&qid=1680491553&s=home-garden&sprefix=smokeless%2Bkorean%2Bbbq%2Cgarden%2C149&sr=1-3&th=1"

# to find headers go to http://myhttpheader.com/ and ad as many headers as needed to access the webpage's HTML code otherwise you might just print out Captcha page
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Cookie": "PHPSESSID=36210c8375c07be9875b646bf706e178; _ga=GA1.2.1555445845.1680491697; _gid=GA1.2.1918107518.1680491697; _gat=1",
    "upgrade-insecure-requests": "1",
    "sec-fetch-site": "cross-site",

}

r = requests.get(url=URL, headers=header)
amazon_item_webpage_html = r.text
# print to confirm that you are accessing the HTML and not just the Captcha page
# print(amazon_item_webpage_html)

soup = BeautifulSoup(amazon_item_webpage_html, "lxml")
item_price = soup.find(name="span", class_="a-price-whole")
item_price_as_whole_num = int(item_price.getText().split(".")[0])
print(item_price_as_whole_num)

TARGET_PRICE = 100
MY_EMAIL = "shotokillua55@gmail.com"
PASSWORD = "hwoxibxdpyngtimt"

item_name = soup.find(id="productTitle").getText().strip()
print(item_name)

if item_price_as_whole_num < TARGET_PRICE:
    message = f"{item_name} is now ${item_price_as_whole_num}!"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Amazon Low Price Alert!\n\n{message}\n{URL}",
        )