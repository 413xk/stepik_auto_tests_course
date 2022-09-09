import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    (browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')).click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = (browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value')).text
    result = math.log(abs(12*math.sin(int(x_element))))

    (browser.find_element(By.CSS_SELECTOR, 'input#answer')).send_keys(result)

    (browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')).click()

    alert_text = browser.switch_to.alert.text
    number = alert_text.split(': ')[-1]

    #  how to send answer to stepic?
   # browser.get('https://stepik.org/lesson/184253/step/4?unit=158843')
   # answer = browser.find_element(By.CSS_SELECTOR, "div[data-type='string-quiz']")
   # answer.send_keys(number)

finally:
    print(browser.switch_to.alert.text)
    browser.quit()

