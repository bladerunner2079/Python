import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import csv
from pathlib import Path


br = RoboBrowser()

# Project URL
br.open("https://market.fuzzwork.co.uk/hub/type/34/")
soup = br.parsed

# Filtering out all order ID's
order_tag = soup.find_all("a", href=True)
order_id_list = []

for el in order_tag:
    if "history" in el["href"]:
        order_id_list.append(el.string)

order_id_list = list(set(order_id_list))


# Actual parsing
tag = soup.find_all("td")
export_dict = {}
price_prev = 0 # Separating data between buy & sell prices
file_directory = Path("C:/Users/edgar/PycharmProjects/working_web/volume_data.csv") # File directory


for idx, el in enumerate(tag):
    if el.string in order_id_list:
        # print(tag[idx])
        # print(tag[idx+2])
        # print(tag[idx+4])
        # print(tag[idx+6])

        # Export data adjustments
        order_id = int(tag[idx].string)
        volume = int(tag[idx+2].string.split("/")[0].replace(",", ""))
        price = int(tag[idx+4].string.replace(",", "").replace(".", ""))/100
        location = tag[idx+6].string

        if price_prev <= price:

            # Export data
            export_dict["Order ID"] = order_id
            export_dict["Volume"] = volume
            export_dict["Price"] = price
            export_dict["Location"] = location

            fieldnames = [*export_dict]

            # Checking if file exists
            if file_directory.is_file() is True:
                write_head = False
            else:
                write_head = True

            with open('volume_data.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                if write_head is True:
                    writer.writeheader()

                writer.writerow(export_dict)
            price_prev = price


print(export_dict)
