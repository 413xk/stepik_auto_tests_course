# Я хз, он не кидает ошибку, даже если вручную три поля искать, он одно пропускает и идет дальше

import string
import random

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #  Ищем по локатору обязательные поля
    required_fields = browser.find_elements(By.CSS_SELECTOR, 'input:required')

    #  Проходимся по ним циклом и заполняем рандомными буквами
    for i in required_fields:
        letters = string.ascii_lowercase
        random_word = ''.join(random.choice(letters) for _ in range(random.randrange(5, 10)))
        i.send_keys(random_word)
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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
