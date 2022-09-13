#  lesson6_step4.py
# test
import math
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_xpath_form')
    elements = browser.find_elements(By.XPATH, '//input')
    for element in elements:
        letters = string.ascii_lowercase
        random_word = ''.join(random.choice(letters) for _ in range(8))
        element.send_keys(random_word)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
