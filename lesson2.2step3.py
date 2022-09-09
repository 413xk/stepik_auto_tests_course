import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')

    summary = int((browser.find_element(By.ID, 'num1')).text) + int((browser.find_element(By.ID, 'num2')).text)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(summary))

    (browser.find_element(By.CSS_SELECTOR, 'button.btn-default')).click()



finally:
    time.sleep(7)
    browser.quit()

