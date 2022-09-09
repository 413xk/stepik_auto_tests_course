import random
import string
import time
import os

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By



try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    # generator of random word
    def rand_word():
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 10)))

    (browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")).send_keys(rand_word())
    (browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")).send_keys(rand_word())
    (browser.find_element(By.CSS_SELECTOR, "input[name='email']")).send_keys(rand_word())

    #  attach file
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    attach_file = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    attach_file.send_keys(file_path)

    (browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')).click()


finally:
    time.sleep(3)
    browser.quit()
