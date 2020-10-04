from selenium import webdriver
from time import sleep
from tinder_login import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Firefox()


    def login(self):
        self.driver.get("https://tinder.com")
        sleep(2)

        # More option button
        more_options_btn = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div[3]/span/button")
        more_options_btn.click()
        sleep(2)


        # Log-in with Facebook
        login_btn = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div[3]/span/div[3]/button/span[2]")
        login_btn.click()
        sleep(2)




