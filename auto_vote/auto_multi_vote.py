# Guide from https://www.lambdatest.com/blog/how-to-automate-filling-in-web-forms-with-python-using-selenium/


# Requirements
# pip install selenium
# pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time
import random

# User information
user_dic = {'1':{'name':'Name LastName', 'email' : 'example@example.com'},
            '2':{'name':'Name LastName','email' : 'example@example.com'},
            '3':{'name':'Name LastName', 'email' : 'example@example.com'}}


# Random sleep so the time of voting is not predictable
# random.seed(42)
def vote(name, email):
    # Initiate webdriver
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("https://votar-trajeartesanal.srtacolombia.org/trajeartesanal.html")

    # Click on vote button
    vote_button = browser.find_element(By.XPATH, "//div[@id='trajeartesanalantioquia']/div[2]/button[1]")
    vote_button.click()

    # Delay for form to load
    time.sleep(3)

    # Fill out form
    name_form = browser.find_element(By.XPATH, "//input[@id='lastname']")
    name_form.send_keys(name)

    email_form = browser.find_element(By.XPATH, "//input[@id='email']")
    email_form.send_keys(email)

    # Delay to visualize info
    time.sleep(3)

    # Send vote
    confirm_button = browser.find_element(By.XPATH, "//form[@id='registration']/center[1]/p[1]/button[1]")
    confirm_button.click()

    time.sleep(3)

    browser.quit()

while True:
    for user in user_dic:
        vote(user_dic[user]['name'],user_dic[user]['email'])
        random_time=random.randint(2*60,10*60)
        print('wait:', random_time/60)
        time.sleep(random_time)
    time.sleep((60-2*(len(user_dic.keys())-1))*60)
    
