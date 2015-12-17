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

    browser.get('http://www.bing.com/')  # open bing

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


## --------------------------------------------------------------------------------------------------------- ##

def main():


    ff = webdriver.Firefox()  # open Firefox

    print('Begin Script')

    uname = 'jondavid0117@outlook.com'
    pword = 'P@$$word11'

    sign_in(ff, uname, pword)

    time.sleep(random.randint(20, 100) / 10)  # suspend script to allow for sign in process to complete

    runDailies(ff)

    #runCarousel(ff)

    ff.quit()

    input()

## --------------------------------------------------------------------------------------------------------- ##



main()



