import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# website - cambridge dictionary
def test_search_bar():
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    tests_functions = [
        send_first_word,
        send_second_word,
        send_third_word,
        send_numbers,
        send_nothing,
        send_signs,
        check_english_china_translate
    ]

    for function in tests_functions:
        driver.get("https://dictionary.cambridge.org/")
        textfield = driver.find_element(by=By.NAME, value="q")
        try:
            function(driver)
        except Exception:
            function(textfield)
        time.sleep(1)
    driver.quit()

def send_first_word(textfield):
    textfield.send_keys("Programmer", Keys.ENTER)

def send_second_word(textfield):
    textfield.send_keys("Капитан", Keys.ENTER)

def send_third_word(textfield):
    textfield.send_keys("qwertyui", Keys.ENTER)

def send_numbers(textfield):
    textfield.send_keys("1234567", Keys.ENTER)

def send_nothing(textfield):
    textfield.send_keys("", Keys.ENTER)

def send_signs(textfield):
    textfield.send_keys("!№;%:?", Keys.ENTER)

def check_english_china_translate(driver: WebDriver):
    textfield = driver.find_element(by=By.CSS_SELECTOR, value="cdo-dataset-selector")
    textfield.click()
    eng_ch = driver.find_element(by=By.CSS_SELECTOR, value="hp")
    eng_ch.click()
    textfield = driver.find_element(by=By.NAME, value="q")
    textfield.send_keys("Hello")


test_search_bar()
