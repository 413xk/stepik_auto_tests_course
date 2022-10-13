import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

array_of_links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.mark.parametrize('links', array_of_links)
def test_put_answers(browser, links):
    answer = str(math.log(int(time.time())))
    browser.get(links)
    browser.implicitly_wait(10)
    fill_field = browser.find_element(By.CSS_SELECTOR, '.ember-text-area')
    fill_field.send_keys(answer)
    button = browser.find_element(By.CSS_SELECTOR, 'div.attempt__actions > button')
    browser.implicitly_wait(10)
    button.click()
    correct_answer = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    browser.implicitly_wait(100)
    assert correct_answer == 'Correct!', 'Not correct answer!!!'


if __name__ == '__main__':
    test_put_answers()


