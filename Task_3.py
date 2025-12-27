import time
import faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep


def choose_way():
    select_element = driver.find_element(by=By.CSS_SELECTOR, value="select[name='fromPort']")
    select1 = Select(select_element)
    select1.select_by_value("Portland")
    sleep(1)
    select_element2 = driver.find_element(by=By.CSS_SELECTOR, value="select[name='toPort']")
    select2 = Select(select_element2)
    select2.select_by_index(2)
    sleep(1)
    btn = driver.find_element(by=By.CSS_SELECTOR, value=".btn.btn-primary")
    btn.click()
    sleep(2)

def choose_flight():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@value='Choose This Flight']")))
    buttons = driver.find_elements(by=By.XPATH, value="//input[@value='Choose This Flight']")
    buttons[2].click()
    time.sleep(5)

def set_value(locator, value):
    element = driver.find_element(*locator)
    driver.execute_script(
        "arguments[0].value = arguments[1];",
        element,
        value
    )
    time.sleep(0.5)

def insert_values(faker):
    full_name = faker.name()

    set_value((By.ID, "inputName"), full_name)
    set_value((By.ID, "address"), faker.address())
    set_value((By.NAME, "city"), faker.city())
    set_value((By.ID, "state"), faker.state())
    set_value((By.ID, "zipCode"), faker.zipcode())
    set_value((By.ID, "creditCardNumber"), faker.credit_card_number())
    set_value((By.ID, "creditCardMonth"), faker.month())
    set_value((By.ID, "creditCardYear"), faker.year())
    set_value((By.ID, "nameOnCard"), full_name)

    driver.find_element(by=By.XPATH, value="//input[@type='checkbox']").click()
    driver.find_element(by=By.CSS_SELECTOR, value=".btn.btn-primary").click()
    sleep(5)


driver = webdriver.Chrome()
driver.get("https://blazedemo.com/")
faker = faker.Faker()
sleep(0.5)
choose_way()
choose_flight()
insert_values(faker)
driver.quit()