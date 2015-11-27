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


browser = webdriver.Firefox()  # open Firefox



uname = sys.argv[1]
pword = sys.argv[2]


# sign in to bing
def sign_in(email, password):
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


# create list of search terms

search_list = ['doustopped', 'immeasurableness', 'sextette', 'penthouse', 'payette', 'oarfishes', 'pollutedness',
               'leucocythaemia', 'baldomero', 'misbehavior', 'ankylotic', 'unelected', 'englacial', 'vinie',
               'vorticella', 'camwood', 'noninferable', 'chylous', 'subitem', 'preexploded', 'foggia', 'subpubic',
               'interclass', 'outthrusting', 'acinacifolious', 'amrita', 'gape', 'cauld', 'cain', 'nonexpiry',
               'resourcefully', 'recon', 'thir', 'diatropism', 'influential', 'permalloy', 'uninvented', 'velouria',
               'luminance', 'krebs', 'langmuir', 'guayaberas', 'bertrant', 'thereby', 'triploblastic', 'unarithmetical',
               'decomposable', 'knobbier', 'strachey', 'whichever', 'ledger', 'intransigent', 'letting', 'onassis',
               'nonanachronous', 'rappelling', 'deciare', 'solariums', 'misreward', 'soliloquised', 'carthaginian',
               'geomorphology', 'overworking', 'antitheology', 'gardena', 'sourceful', 'supersensuality', 'fidget',
               'hypocaust', 'lipocaic', 'duellist', 'untheatrical', 'metrics', 'babbler', 'supremacy', 'reclaimant',
               'heartedly', 'disharmony', 'perdured', 'marled', 'baalistic', 'easylike', 'airliner', 'prosopopoeia',
               'prophets', 'arbitrarily', 'intermunicipal', 'poyntill', 'jansenism', 'democratising', 'makah',
               'flavorous', 'pommelled', 'nonbreaching', 'intent', 'anteprandial', 'neuritic', 'resaleable',
               'unremembered', 'unpenetrating']


# loop search using random searching method
def search_loop(n):  # n is an integer

    browser.get('http://www.bing.com/')  # open bing

    for i in range(0, n):
        search_term = search_list[random.randint(0, 99)]  # set random search term
        elem = browser.find_element_by_name("q")  # Find the search box
        elem.send_keys(search_term + Keys.RETURN)  # Enter random search term from list
        browser.get("http://www.bing.com/")  # open bing
        time.sleep(5.0)  # pause time






## --------------------------------------------------------------------------------------------------------- ##

def main():
    print('Begin Script')

    sign_in(uname, pword)

    time.sleep(random.randint(20, 100) / 10)  # suspend script to allow for sign in process to complete

    search_loop(30)

    browser.quit()

## --------------------------------------------------------------------------------------------------------- ##



#main()



