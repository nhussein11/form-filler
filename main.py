
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

import time
from random import randint


def random_html_elements_selection(html_elements: list) -> int:
    return randint(1, len(html_elements)-1)


def fill_form():
    sections = driver.find_elements(By.CLASS_NAME, "Qr7Oae")

    for section in sections[:-2]:
        radio_buttons = section.find_elements(By.CLASS_NAME, "Od2TWd")
        random_selection = random_html_elements_selection(radio_buttons)

        driver.execute_script("arguments[0].click();", radio_buttons[random_selection])
        time.sleep(0.25)

    check_boxs = sections[-2].find_elements(By.CLASS_NAME, "uHMk6b")
    random_selection = random_html_elements_selection(check_boxs)
    check_boxs[random_selection].click()

    send_button = driver.find_element(By.CLASS_NAME, "uArJ5e")
    send_button.click()

#Enter your URL here
URL = "(here)"

options = Options()

#Uncomment this line if you want to run the script without opening a new window
# options.add_argument('--headless')

driver = webdriver.Firefox(service=Service(
    GeckoDriverManager().install()), options=options)

for i in range(1000):
    driver.get(URL)
    fill_form()
    time.sleep(0.25)
