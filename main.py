
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
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "Od2TWd"))).click()
        radio_buttons = section.find_elements(By.CLASS_NAME, "Od2TWd")
        random_selection = random_html_elements_selection(radio_buttons)
        radio_buttons[random_selection].click()
        time.sleep(0.5)

    check_boxs = sections[-2].find_elements(By.CLASS_NAME, "uHMk6b")
    random_selection = random_html_elements_selection(check_boxs)
    check_boxs[random_selection].click()

    send_button = driver.find_element(By.CLASS_NAME, "uArJ5e")
    send_button.click()

#Enter your URL here
URL = "(here)"

options = Options()
# options.add_argument('--headless')

driver = webdriver.Firefox(service=Service(
    GeckoDriverManager().install()), options=options)

for i in range(10):
    driver.get(URL)
    fill_form()
    driver.close()
