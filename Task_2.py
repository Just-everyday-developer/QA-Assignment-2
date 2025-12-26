from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def login(username, password):
    field_1 = driver.find_element(by=By.NAME, value="username")
    field_1.send_keys(username)
    sleep(0.5)
    field_2 = driver.find_element(by=By.NAME, value="password")
    field_2.send_keys(password)
    sleep(0.5)
    submit_btn = driver.find_element(By.CLASS_NAME, value="btn")
    try:
        submit_btn.click()
        logout()
    except Exception:
        print("Couldn't cope =(")
        print("Error message from website:", driver.find_element(by=By.ID, value="error").text)
    sleep(0.5)


def logout():
    log_out_btn = driver.find_element(by=By.LINK_TEXT, value="Log out")
    log_out_btn.click()
    sleep(1)


driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

login(username="student", password="Password123")  # Successful login
sleep(0.5)
login(username="incorrectUser", password="Password123")  # Incorrect username, correct password
sleep(0.5)
login(username="student", password="incorrectPassword")  # Incorrect password, correct username
sleep(0.5)
login(username="", password="")  # empty values
sleep(0.5)

driver.quit()



