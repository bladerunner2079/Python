
from selenium import webdriver

# Open FireFox web browser and go to URL
driver = webdriver.Firefox()
driver.get("http://econpy.pythonanywhere.com/ex/001.html")

# Extract data of "buyers" & "sellers"
buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

# Print data
num_page_item = len(buyers)
for i in range(num_page_item):
    print(buyers[i].text + " : " + prices[i].text)

driver.close()