import pytest
from config.urls import *
from selenium.webdriver.common.by import By
from config.elements_and_path.header import *
from functions.check_up import *

@pytest.mark.ui
def test_header(browser):
    """Тест проверки блока Header"""
    
    browser.get(BASE_URL_NORMAL)
    wait_for_page_load(browser) # ждем загрузки страницы
    
    # Проверяем, что блок header виден и существует
    safe_find_and_verify(browser, By.XPATH, HEADER, "HEADER")


    # Проверяем, что в блоке header содержится кнопка "Обуждение" со ссылкой на "https://ru.wikipedia.org/wiki/Служебная:Мое_обсуждение"(в sha256)
    safe_find_and_verify_href(browser, By.XPATH, HEADER_BUTTON_TRAINING, "Обсуждение", HEADER_BUTTON_TRAINING_BEFORE_URL)

    # Кликаем по кнопке "Обуждение" и проверяем, что переходим на страницу "https://ru.wikipedia.org/wiki/Обсуждение_участника{ip}"(в sha256)
    safe_click_and_verify_contains(browser, By.XPATH, HEADER_BUTTON_TRAINING, "Обсуждение", HEADER_BUTTON_TRAINING_AFTER_URL)
    wait_for_page_load(browser) # ждем загрузки страницы
    safe_back_and_verify(browser, BASE_URL_FACT) # возвращаемся назад на главную страницу


    # Проверяем, что в блоке header содержится кнопка "Вклад" со ссылкой на "https://ru.wikipedia.org/wiki/Служебная:Мой_вклад"(в sha256)"
    safe_find_and_verify_href(browser, By.XPATH, HEADER_BUTTON_DEPOSIT, "Вклад", HEADER_BUTTON_DEPOSIT_URL)

    # Кликаем по кнопке "Вклад" и проверяем, что переходим на страницу "https://ru.wikipedia.org/wiki/Служебная:Мой_вклад"(в sha256)
    safe_click_and_verify_contains(browser, By.XPATH, HEADER_BUTTON_DEPOSIT, "Вклад", HEADER_BUTTON_DEPOSIT_AFTER_URL)
    wait_for_page_load(browser) # ждем загрузки страницы
    safe_back_and_verify(browser, BASE_URL_FACT) # возвращаемся назад на главную страницу


    # Проверяем, что в блоке header содержится кнопка "Создать учетную запись" со ссылкой на "https://ru.wikipedia.org/wiki/Служебная:Создать_учетную_запись"(в sha256)
    safe_find_and_verify_href(browser, By.XPATH, HEADER_BUTTON_CREATE_ACCOUNT, "Создать учетную запись", HEADER_BUTTON_CREATE_ACCOUNT_URL)

    # Кликаем по кнопке "Создать учетную запись" и проверяем, что переходим на страницу "https://ru.wikipedia.org/wiki/Служебная:Создать_учетную_запись"(в sha256)
    safe_click_and_verify_contains(browser, By.XPATH, HEADER_BUTTON_CREATE_ACCOUNT, "Создать учетную запись", HEADER_BUTTON_CREATE_ACCOUNT_AFTER_URL)
    wait_for_page_load(browser) # ждем загрузки страницы
    safe_back_and_verify(browser, BASE_URL_FACT) # возвращаемся назад на главную страницу


    # Проверяем, что в блоке header содержится кнопка "Войти" со ссылкой на "https://ru.wikipedia.org/wiki/Служебная:Вход"(в sha256)
    safe_find_and_verify_href(browser, By.XPATH, HEADER_BUTTON_LOGIN, "Войти", HEADER_BUTTON_LOGIN_URL)

    # Кликаем по кнопке "Войти" и проверяем, что переходим на страницу "https://ru.wikipedia.org/wiki/Служебная:Вход"(в sha256)
    safe_click_and_verify_contains(browser, By.XPATH, HEADER_BUTTON_LOGIN, "Войти", HEADER_BUTTON_LOGIN_AFTER_URL)
    wait_for_page_load(browser) # ждем загрузки страницы
    safe_back_and_verify(browser, BASE_URL_FACT) # возвращаемся назад на главную страницу


    # Проверяем, что логотип википедии виден, существует и имеет ссылку, переходит на "https://ru.wikipedia.org/wiki/Заглавная_страница"(в sha256)
    safe_find_and_verify_href(browser, By.XPATH, LOGO, "Логотип Википедии", BASE_URL_FACT)
    safe_click_and_verify(browser, By.XPATH, LOGO, "Логотип Википедии", BASE_URL_FACT)
    wait_for_page_load(browser) # ждем загрузки страницы