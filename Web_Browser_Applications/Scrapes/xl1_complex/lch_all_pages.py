
from selenium import webdriver

# Dependencies
max_page_num = 5
max_page_dig = 3
driver = webdriver.Firefox()

with open("price_data.csv", "w") as f:
    f.write("Buyer, Price \n")


for i in range(1, max_page_num + 1):
    page_num = (max_page_dig - len(str(i))) * "0" + str(i)
    url = "http://econpy.pythonanywhere.com/ex/" + page_num + ".html"

    driver.get(url)

    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

    num_page_items = len(buyers)
    with open("price_data.csv", "a") as f:
        for i in range(num_page_items):
            f.write(buyers[i].text + "," + prices[i].text + "\n")


driver.close()f