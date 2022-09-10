
from inspect import _void
from tabnanny import check
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
    # print((len(html_elements)-1))
    return randint(0, len(html_elements)-1)


def fill_form():
    sections = driver.find_elements(By.CLASS_NAME, "Qr7Oae")

    fill_radio_buttons_arbitrarily(sections[0])
    fill_radio_buttons_arbitrarily(sections[1])

    fill_check_boxs_positive(sections[2])    # 95 % DE ESTAS
    # fill_section_3_negative(sections[2])   # 5 % DE ESTAS

    fill_radio_buttons_positive(sections[3]) # 80% POSITIVAS
    # fill_section_negative(sections[3])     # 20% NEGATYIVAS

    fill_radio_buttons_positive(sections[4]) #  90% POSITIVAS
    # fill_section_negative(sections[4])     #  10% NEGATIVAS

    fill_check_boxs_arbitrarily(sections[5]) 

    fill_multiples_check_boxs_arbitrarily(sections[6], 2)  #TODO: TENDENCIOSA PARA LAS 5 PRIMERAS

    fill_multiples_check_boxs_arbitrarily(sections[7], 4) 

    fill_multiples_check_boxs_arbitrarily(sections[8], 3)

    fill_radio_buttons_arbitrarily(sections[9])

    fill_multiples_check_boxs_arbitrarily(sections[10], 2)

    fill_radio_buttons_arbitrarily(sections[11])            #TODO: TENDENCIOSA PARA LAS 2 ULTIMAS

    # send_button = driver.find_element(By.CLASS_NAME, "uArJ5e")
    # send_button.click()


def fill_radio_buttons_arbitrarily(html_elements: list):
    radio_buttons = html_elements.find_elements(By.CLASS_NAME, "Od2TWd")
    random_selection = random_html_elements_selection(radio_buttons)
    driver.execute_script(
        "arguments[0].click();", radio_buttons[random_selection])
    time.sleep(0.25)


def fill_radio_buttons_positive(html_elements: list):
    radio_buttons = html_elements.find_elements(By.CLASS_NAME, "Od2TWd")
    driver.execute_script(
        "arguments[0].click();", radio_buttons[0])
    time.sleep(0.25)


def fill_radio_buttons_negative(html_elements: list):
    radio_buttons = html_elements.find_elements(By.CLASS_NAME, "Od2TWd")
    driver.execute_script(
        "arguments[0].click();", radio_buttons[-1])
    time.sleep(0.25)


def fill_check_boxs_arbitrarily(html_elements: list):
    check_boxs = html_elements.find_elements(By.CLASS_NAME, "uVccjd")
    random_selection = random_html_elements_selection(check_boxs)
    check_boxs[random_selection].click()
    time.sleep(0.25)


def fill_multiples_check_boxs_arbitrarily(html_elements: list, iterations: int):
    check_boxs = html_elements.find_elements(By.CLASS_NAME, "uVccjd")
    print(len(check_boxs))
    random_iterations = randint(1, iterations)
    for i in range(random_iterations):
        random_selection = random_html_elements_selection(check_boxs)
        check_boxs[random_selection].click()
        time.sleep(0.25)


def fill_check_boxs_positive(html_elements: list):
    check_boxs = html_elements.find_elements(By.CLASS_NAME, "uVccjd")
    random_iterations = randint(0, len(check_boxs[:-1]))
    for i in range(random_iterations):
        random_selection = random_html_elements_selection(check_boxs[:-1])
        if not check_boxs[random_selection].is_selected():
            check_boxs[random_selection].click()


def fill_check_boxs_negative(html_elements: list):
    check_box = html_elements.find_elements(By.CLASS_NAME, "uHMk6b")
    check_box[-1].click()


URL = "https://forms.gle/y4UJXBEHdojHos2eA"

options = Options()
driver = webdriver.Firefox(service=Service(
    GeckoDriverManager().install()), options=options)

for i in range(10):
    driver.get(URL)
    fill_form()
    time.sleep(0.25)
