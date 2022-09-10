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
    return randint(0, len(html_elements)-1)


def random_trend(tendecy: int) -> int:
    return randint(1, tendecy)


def fill_form(iteration_number: int):
    sections = driver.find_elements(By.CLASS_NAME, "Qr7Oae")

    fill_radio_buttons_arbitrarily(sections[0])
    fill_radio_buttons_arbitrarily(sections[1])

    if iteration_number <= 94:
        fill_check_boxs_positive(sections[2])       # 95 % DE ESTAS
    else:
        fill_check_boxs_negative(sections[2])       # 5 % DE ESTAS

    if iteration_number <= 79:
        fill_radio_buttons_positive(sections[3])    # 80% POSITIVAS
    else:
        fill_radio_buttons_negative(sections[3])    # 20% NEGATYIVAS

    if iteration_number <= 89:
        fill_radio_buttons_positive(sections[4])  # 90% POSITIVAS
        # TODO: TENDENCIOSA PARA LAS 5 PRIMERAS
        if iteration_number <= 95:
            fill_multiples_check_boxs_arbitrarily_with_trend(sections[6], 2, 4)
        else:
            fill_multiples_check_boxs_arbitrarily(sections[6], 2)

        fill_multiples_check_boxs_arbitrarily(sections[7], 4)

        fill_multiples_check_boxs_arbitrarily(sections[8], 3)

        fill_radio_buttons_arbitrarily(sections[9])

        fill_multiples_check_boxs_arbitrarily(sections[10], 2)

        # TODO: TENDENCIOSA PARA LAS 2 ULTIMAS
        if iteration_number <= 95:
            fill_radio_buttons_arbitrarily_with_trend(sections[11], 2)
        else:
            fill_radio_buttons_arbitrarily(sections[11])

    else:
        fill_radio_buttons_negative(sections[4])  # 10% NEGATIVAS
        fill_check_boxs_arbitrarily(sections[5])

    send_button = driver.find_element(By.CLASS_NAME, "Y5sE8d")
    send_button.click()
    print(send_button.is_selected())


def fill_radio_buttons_arbitrarily(html_elements: list):
    radio_buttons = html_elements.find_elements(By.CLASS_NAME, "Od2TWd")
    random_selection = random_html_elements_selection(radio_buttons)
    driver.execute_script(
        "arguments[0].click();", radio_buttons[random_selection])
    time.sleep(0.25)


def fill_radio_buttons_arbitrarily_with_trend(html_elements: list, tendency: int):
    radio_buttons = html_elements.find_elements(By.CLASS_NAME, "Od2TWd")
    random_selection = random_trend(tendency)
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
    random_iterations = randint(1, iterations)
    for i in range(random_iterations):
        random_selection = random_html_elements_selection(check_boxs)
        check_boxs[random_selection].click()
        time.sleep(0.25)


def fill_multiples_check_boxs_arbitrarily_with_trend(html_elements: list, iterations: int, tendency: int):
    check_boxs = html_elements.find_elements(By.CLASS_NAME, "uVccjd")
    random_iterations = randint(1, iterations)
    for i in range(random_iterations):
        random_selection = random_trend(tendency)
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

for i in range(1):
    driver.get(URL)
    fill_form(i)
    time.sleep(0.25)
