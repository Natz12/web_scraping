# https://votar-trajeartesanal.srtacolombia.org/trajeartesanal.html
# https://ecommerce-playground.lambdatest.io/index.php?route=account/register
# Guide from https://www.lambdatest.com/blog/how-to-automate-filling-in-web-forms-with-python-using-selenium/
# pip install selenium
# pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time
import random


name = 'Natalia Hoyos'
email = 'natahoy12@gmail.com'

random.seed(42)
random_time=random.randint(1,5)
time.sleep(random_time)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://votar-trajeartesanal.srtacolombia.org/trajeartesanal.html")

vote_button = browser.find_element(By.XPATH, "//div[@id='trajeartesanalantioquia']/div[2]/button[1]")
vote_button.click()

time.sleep(3)
name_form = browser.find_element(By.XPATH, "//input[@id='lastname']")
name_form.send_keys(name)

email_form = browser.find_element(By.XPATH, "//input[@id='email']")
email_form.send_keys(email)

time.sleep(1)
confirm_button = browser.find_element(By.XPATH, "//form[@id='registration']/center[1]/p[1]/button[1]")
confirm_button.click()

browser.quit()