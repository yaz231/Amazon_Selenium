from selenium import webdriver
import time

usr = ''
pswd = ''
item = ''
url = ''

def login():
    driver.find_element_by_id('nav-link-accountList').click()
    #Email Address
    driver.find_element_by_id('ap_email').send_keys(usr)
    driver.find_element_by_id('continue').click()
    #Password
    driver.find_element_by_id('ap_password').send_keys(pswd)
    driver.find_element_by_id('signInSubmit').click()

def search_item():
    if url != '':
        driver.get(url)
    else:
        driver.find_element_by_id('field-keywords').send_keys(item)
        driver.find_element_by_id('nav-search-submit-text').click()

def insta_buy():
    try:
        driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[7]/div[6]/div[1]/div[5]/div/div/div[1]/div/div/div[1]/div/div[1]/a').click()
        driver.find_element_by_id('buy-now-button').click()
        driver.find_element_by_id('turbo-checkout-pyo-button').click()
    except:
        driver.quit()

def monitor_cart():
    driver.find_element_by_id('nav-cart').click()
    cart = driver.find_elements_by_class_name('sc-list-item-content')
    time.sleep(2)
    for element in cart:
        element.find
        name = element.find_element_by_xpath('//*[@class="a-row sc-list-item sc-list-item-border sc-java-remote-feature"]/div[4]/div/div[1]/div/div/div[2]/ul/li[1]/span/a/span[1]')
        # print(name.text)
        time.sleep(1)
        break
        # price = element.find_elements_by_class_name('a-size-large a-color-base sc-price sc-white-space-nowrap sc-product-price a-text-bold')
        # print("Name: " + name.text + "     Price: " + price.text)

if __name__ == "__main__":
    usr = input("Enter Amazon account username: ")
    pswd = input("Enter Amazon account password: ")
    item = input("Enter item name to search or the URL of the item: ")
    # usr = ''
    # pswd = ''
    item = 'https://www.amazon.com/PB2-Powdered-Chocolate-Peanut-Butter/dp/B07W7TZ551/ref=sr_1_8?dchild=1&keywords=pb2&qid=1603263453&sr=8-8'
    if item.find('.com'):
        url = item
    driver = webdriver.Edge(executable_path="C:\Program Files (x86)\msedgedriver.exe")
    driver.get("http://amazon.com")
    login()
    # search_item()
    # insta_buy()
    monitor_cart()