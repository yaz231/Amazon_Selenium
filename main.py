from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

usr = ''
pswd = ''
item = ''
url = ''

def login():
    driver.find_element_by_id('nav-link-accountList').click()
    time.sleep(1)
    try:
        user = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'ap_email'))
        )
        driver.find_element_by_id('ap_email').send_keys(usr)
        driver.find_element_by_id('continue').click()
        password = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'ap_password'))
        )
        driver.find_element_by_id('ap_password').send_keys(pswd)
        driver.find_element_by_id('signInSubmit').click()
    except:
        driver.quit()


def login2():
    driver.find_element_by_class_name('nav-complex-inner').click()
    #Email Address
    time.sleep(2)
    # driver.find_element_by_tag_name('signEmail').send_keys(usr)
    driver.find_element_by_id('labeled-input-signEmail').send_keys(usr)
    time.sleep(2)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    #Password
    time.sleep(2)
    driver.find_element_by_id('labeled-input-password').send_keys(pswd)
    driver.find_element_by_xpath('//button[@type="submit"]').click()


def search_item():
    if url != '':
        driver.get(url)
    else:
        driver.find_element_by_id('field-keywords').send_keys(item)
        driver.find_element_by_id('nav-search-submit-text').click()


def search_item2():
    if url != '':
        driver.get(url)
    else:
        driver.find_element_by_id('SearchBox2020').send_keys(item)
        driver.find_element_by_class_name('header2020-search-button').click()
        items = driver.find_elements_by_class_name('item-cell')
        for element in items:
            # name = element.find_element_by_xpath('//*[@id="app"]/div[2]/section/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[cnt]/div/div[1]/a')
            name = element.find_element_by_class_name('item-title')
            print(name.text)


def insta_buy():
    try:
        driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[7]/div[6]/div[1]/div[5]/div/div/div[1]/div/div/div[1]/div/div[1]/a').click()
        driver.find_element_by_id('buy-now-button').click()
        driver.find_element_by_id('turbo-checkout-pyo-button').click()
    except:
        driver.quit()


def monitor_cart():
    driver.find_element_by_id('nav-cart').click()
    try:
        items = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@id, 'sc-item-')]"))
        )
        cart = driver.find_elements_by_xpath("//*[contains(@id, 'sc-item-')]")
        for element in cart:
            print(element.text)
            time.sleep(3)
    except:
        driver.quit()



if __name__ == "__main__":
    usr = input("Enter Amazon account username: ")
    pswd = input("Enter Amazon account password: ")
    item = input("Enter item name to search or the URL of the item: ")
    if item.find('.com'):
        url = item
    else:
        url = ''
    driver = webdriver.Edge(executable_path="C:\Program Files (x86)\msedgedriver.exe")
    driver.get("http://amazon.com")
    # login()
    # login2()
    # search_item()
    # search_item2()
    # insta_buy()
    # monitor_cart()