from selenium.webdriver.common.by import By
from random import randint

def random_html_elements_selection(html_elements: list) -> int:
    return randint(1, len(html_elements)-1)

def fill_section_0(html_elements: list, ):
        radio_buttons = html_elements.find_elements(By.CLASS_NAME, "Od2TWd")
        print(len(radio_buttons))
        random_selection = random_html_elements_selection(radio_buttons)
                # driver.execute_script(
        #     "arguments[0].click();", radio_buttons[random_selection])
        time.sleep(0.25)