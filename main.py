
from inspect import _void
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from random import randint

import time


def random_html_elements_selection(html_elements: list) -> int:
    return randint(1, len(html_elements)-1)


def fill_form():
    sections = driver.find_elements(By.CLASS_NAME, "Qr7Oae")

    fill_section_arbitrarily(sections[0])
    fill_section_arbitrarily(sections[1])
    fill_section_3_positive(sections[2])
# for section in sections:
#     radio_buttons = section.find_elements(By.CLASS_NAME, "Od2TWd")
#     print(len(radio_buttons))
#     random_selection = random_html_elements_selection(radio_buttons)

#     driver.execute_script(
#         "arguments[0].click();", radio_buttons[random_selection])
#     time.sleep(0.25)

# check_boxs = sections[-2].find_elements(By.CLASS_NAME, "uHMk6b")
# random_selection = random_html_elements_selection(check_boxs)
# check_boxs[random_selection].click()

# send_button = driver.find_element(By.CLASS_NAME, "uArJ5e")
# send_button.click()


def fill_section_arbitrarily(html_elements: list):
    radio_buttons = html_elements.find_elements(By.CLASS_NAME, "Od2TWd")
    random_selection = random_html_elements_selection(radio_buttons)
    driver.execute_script(
        "arguments[0].click();", radio_buttons[random_selection])
    time.sleep(0.25)


# def fill_section_3_positive(html_elements: list):
#     check_boxs = html_elements.find_elements(By.CLASS_NAME, "uVccjd")
#     random_selection = random_html_elements_selection(check_boxs[:-1])
#     check_boxs[random_selection].click()


# def fill_section_3_negative(html_elements: list):
#     check_box = html_elements[-1].find_elements(By.CLASS_NAME, "uHMk6b")
#     check_box[0].click()


URL = "https://forms.gle/y4UJXBEHdojHos2eA"

options = Options()
driver = webdriver.Firefox(service=Service(
    GeckoDriverManager().install()), options=options)

for i in range(10):
    driver.get(URL)
    fill_form()
    time.sleep(0.25)
