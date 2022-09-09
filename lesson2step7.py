import math
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')

    x_letter = browser.find_element(By.CSS_SELECTOR, 'img#treasure[src]')
    x_element = x_letter.get_attribute('valuex')

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    y_element = calc(x_element)

    input_answer = browser.find_element(By.CSS_SELECTOR, 'input#answer[required]')
    input_answer.send_keys(y_element)

    (browser.find_element(By.CSS_SELECTOR, '#robotCheckbox[required]')).click()
    (browser.find_element(By.CSS_SELECTOR, "#robotsRule[value='robots']")).click()

    (browser.find_element(By.CSS_SELECTOR, 'button.btn-default')).click()

    time.sleep(7)


finally:
    browser.quit()