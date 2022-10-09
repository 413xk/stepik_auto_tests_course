
import unittest
from unittest import TestCase
import string
import random

from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class TestLink(unittest.TestCase):

    def test_links1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        #  Ищем по локатору обязательные поля
        #  required_fields = browser.find_elements(By.CSS_SELECTOR, 'input:required')

        #  Проходимся по ним циклом и заполняем рандомными буквами
        '''for i in required_fields:
            letters = string.ascii_lowercase
            random_word = ''.join(random.choice(letters) for _ in range(random.randrange(5, 10)))
            i.send_keys(random_word)'''

        def random_word():
            letters = string.ascii_lowercase
            random_word = ''.join(random.choice(letters) for _ in range(random.randrange(5, 10)))
            return random_word

        name = browser.find_element(By.CSS_SELECTOR, '.first_class input:required')
        name.send_keys(random_word())
        second_name = browser.find_element(By.CSS_SELECTOR, '.second_class input:required')
        second_name.send_keys(random_word())
        email = browser.find_element(By.CSS_SELECTOR, '.third_class input:required')
        email.send_keys(random_word())

        time.sleep(2)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text


        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Well done')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_links2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        def random_word():
            letters = string.ascii_lowercase
            random_word = ''.join(random.choice(letters) for _ in range(random.randrange(5, 10)))
            return random_word

        name = browser.find_element(By.CSS_SELECTOR, '.first_class input:required')
        name.send_keys(random_word())
        second_name = browser.find_element(By.CSS_SELECTOR, '.second_class input:required')
        second_name.send_keys(random_word())
        email = browser.find_element(By.CSS_SELECTOR, '.third_class input:required')
        email.send_keys(random_word())

        time.sleep(5)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Well done!')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()

    if __name__ == '__main__':
        test_links1()
        test_links2()
