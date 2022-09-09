import math

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://SunInJuly.github.io/execute_script.html')

    x_element = (browser.find_element(By.CSS_SELECTOR, 'span#input_value')).text
    result = str(math.log(abs(12 * math.sin(int(x_element)))))

    inp = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    browser.execute_script("window.scrollBy(0, 100);")
    inp.send_keys(result)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()

    robots_rule = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    robots_rule.click()

    (browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')).click()

    time.sleep(5)

finally:
    browser.quit()