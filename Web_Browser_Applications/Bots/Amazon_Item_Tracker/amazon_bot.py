from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import re
import time


class AmazonBot(object):
    def __init__(self, items):
        self.amazon_url = "https://www.amazon.co.uk/"
        self.items = items

        self.profile = webdriver.Firefox()
        self.options = Options()
        self.driver = webdriver.Firefox()
        self.driver.get(self.amazon_url)


    def search_items(self):
        urls = []
        prices = []
        names = []

        for item in self.items:
            print(f"Searching for {item}...")
            self.driver.get(self.amazon_url)

            # Entering input to the amazon search bar
            search_input = self.driver.find_element_by_id("twotabsearchtextbox")
            search_input.send_keys(item)
            time.sleep(2)

            # Selecting and clicking on the search button
            search_button = self.driver.find_element_by_xpath(
                "/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input")
            search_button.click()
            time.sleep(2)

            t = self.driver.find_element_by_id("result_0")
            asin = t.get_attribute("data-asin")
            url = "https://www.amazon.co.uk/" + asin
            price = self.get_product_price(url)
            name = self.get_product_name(url)

            prices.append(price)
            urls.append(url)
            names.append(name)

            print(price)
            print(name)
            print(url)

            time.sleep(2)

        return prices, urls, names


    def get_product_price(self, url):
        self.driver.get(url)
        try:
            price = self.driver.find_element_by_id("priceblock_ourprice").text
        except:
            pass
        try:
            price = self.driver.find_element_by_id("priceblock_dealprice").text
        except:
            pass
        if price is None:
            price = "Not Available"
        else:
            non_decimal = re.compile(r'[^\d.]+')
            price = non_decimal.sub('', price)
        return price


    def get_product_name(self):
        self.driver.get(url)
        try:
            product_name = self.driver.find_element_by_id("productTitle").text
        except:
            pass
        if product_name is None:
            product_name = "Not Available"


    def end_session(self):
        self.driver.close()



