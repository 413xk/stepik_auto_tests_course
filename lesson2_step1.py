import math
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')
    x_element = browser.find_element(By.CSS_SELECTOR, 'label span#input_value')
    x = x_element.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)

    inp = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    inp.send_keys(y)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    robot_checkbox.click()

    robot_radiobutton = browser.find_element(By.CSS_SELECTOR, 'input.form-check-input#robotsRule')
    robot_radiobutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn-default')
    submit.click()

    time.sleep(10)


finally:
    browser.quit()
