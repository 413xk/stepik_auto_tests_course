import math
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    (browser.find_element(By.CSS_SELECTOR, 'button.trollface.btn')).click()

    browser.switch_to.window(browser.window_handles[1])

    x_element = (browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value')).text
    result = math.log(abs(12*math.sin(int(x_element))))

    (browser.find_element(By.CSS_SELECTOR, 'input#answer')).send_keys(result)
    (browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')).click()
    answer = (browser.switch_to.alert.text.split(' '))[-1] # answer from alert

finally:
    print(answer)
    browser.quit()