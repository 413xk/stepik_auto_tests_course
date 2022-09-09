import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(3)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '$100')
    )

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value').text
    result = math.log(abs(12*math.sin(int(x_element))))

    browser.find_element(By.ID, 'answer').send_keys(str(result))
    button = browser.find_element(By.CSS_SELECTOR, 'button#solve')
    button.click()

    alert_text= browser.switch_to.alert.text
    print(alert_text.split(' ')[-1])

finally:
    time.sleep(5)
    browser.quit()




