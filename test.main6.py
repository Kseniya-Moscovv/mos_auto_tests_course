from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/selects1.html"


def calc(a, b):
    return str(int(a) + int(b))

try:
    browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    browser.get(link)

    a_num = browser.find_element(By.ID, "num1")
    a = a_num.text

    b_num = browser.find_element(By.ID, "num2")
    b = b_num.text

    x = calc(a, b)

    browser.find_element(By.ID, "dropdown").click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{x}']").click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()


