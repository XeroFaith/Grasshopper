#!/usr/bin/python3


"""
Author: XeroFaith
Purpose: script to automate Bing searches
Method: Step 1: automate searches. Step 2: Step 3: Profit!

Requirements: selenium, python 3.4.0, firefox

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

# uname = sys.argv[1]
# pword = sys.argv[2]


# sign in to bing
def sign_in(browser, email, password):
    browser.get("https://login.live.com/")  # open outlook.com


    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "loginfmt"))
        )
    finally:
        login_elem = browser.find_element_by_name("loginfmt")

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "passwd"))
        )
    finally:
        password_elem = browser.find_element_by_name("passwd")

    login_elem.send_keys(email)
    password_elem.send_keys(password)
    password_elem.send_keys(Keys.ENTER)

    wait_time = random.randint(20, 100) / 10
    time.sleep(wait_time)  # pause time

    browser.get("https://www.bing.com/")
    time.sleep(wait_time)


def runCarousel(browser):

    if (browser.current_url != "https://www.bing.com/"):
        browser.get('https://www.bing.com/')  # open bing

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "crs_itemLink_0"))
        )
    finally:
        carousel_elem = browser.find_element_by_id("crs_itemLink_0")

    href = carousel_elem.get_attribute("href")

    browser.get(href)


    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "nav_right"))
        )
    finally:
        arrow = browser.find_element_by_class_name("nav_right")


    element_count = 0
    carousel_elems = []

    while (element_count < 50):

        try:
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "card"))
            )
        finally:
            carousel_elems = browser.find_elements_by_class_name("card")

            element_count = len(carousel_elems)

            arrow.click()


    hrefs = []

    for item in carousel_elems:
        image = item.find_element_by_xpath("./a[1]")
        href = image.get_attribute("href")
        hrefs.append(href)



    for link in hrefs:
        wait_time = random.randint(10, 50) / 10
        browser.get(link)  # open bing
        time.sleep(wait_time)  # pause time


def runDailies(browser):

    # rewards page
    global hrefs
    browser.get("https://www.bing.com/rewards/dashboard")

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "tileset"))
        )
    finally:
        # dailyPage is the set of all of the gray box groups
        dailypage = browser.find_elements_by_class_name("tileset")

    # classBlock is the singular grab box group
    for classBlock in dailypage:
        title = classBlock.find_element_by_class_name("dashboard-title")


        if (title.text == "Earn and explore"):
            # these are "a" tags that have the hrefs in them
            links = classBlock.find_elements_by_tag_name("a")

            hrefs = []

            for link in links:
                linkText = link.find_element_by_class_name("title")

                if (linkText.text != "Trivia challenge"):

                    href = link.get_attribute("href")
                    hrefs.append(href)

    for href in hrefs:
        wait_time = random.randint(10, 50) / 10
        browser.get(href)  # open bing
        time.sleep(wait_time)  # pause time


def runMobile(browser):



    if (browser.current_url != "https://www.bing.com/"):
        browser.get('https://www.bing.com/')  # open bing

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "pop_tile"))
        )
    finally:
        # dailyPage is the set of all of the gray box groups
        first = browser.find_element_by_class_name("pop_tile")

        firstLink = first.get_attribute("href")

        browser.get(firstLink)

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "card"))
        )
    finally:
        # dailyPage is the set of all of the gray box groups
        cards = browser.find_elements_by_class_name("card")

    hrefs = []

    for card in cards:
        a_tag = card.find_element_by_tag_name("a")
        href = a_tag.get_attribute("href")
        hrefs.append(href)

    for href in hrefs[:25]:
        wait_time = random.randint(10, 50) / 10
        browser.get(href)
        time.sleep(wait_time)  # pause time
## --------------------------------------------------------------------------------------------------------- ##

def main():

    uname = sys.argv[1]
    pword = sys.argv[2]

    print("Account: ",uname,'\n',
          "Begin: ",datetime.date.today(),'\n\n'
          )


    ff = webdriver.Firefox()  # open Firefox

    sign_in(ff, uname, pword)

    time.sleep(random.randint(20, 100) / 10)  # suspend script to allow for sign in process to complete

    runCarousel(ff)

    runDailies(ff)

    ff.quit()

    iOS = webdriver.FirefoxProfile()
    iOS.set_preference("general.useragent.override",
                           "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25")

    iOS_FF = webdriver.Firefox(iOS)

    sign_in(iOS_FF, uname, pword)

    runMobile(iOS_FF)

    iOS_FF.quit()

    print("Account: ",uname,'\n',
          "End: ",datetime.date.today(),'\n\n'
          )
## --------------------------------------------------------------------------------------------------------- ##



main()



