import pytest
from config.urls import *
from selenium.webdriver.common.by import By
from config.elements_and_path.hero import *
from functions.check_up import *

@pytest.mark.ui
def test_hero(browser):
    """Тест проверки блока Hero"""
    
    browser.get(BASE_URL_NORMAL)
    wait_for_page_load(browser) # ждем загрузки страницы
    

    # Проверяем, что кнопка обуждение содержит ссылку на "https://ru.wikipedia.org/wiki/Обсуждение:Заглавная_страница"(в sha256)
    safe_find_and_verify_href(browser, By.XPATH, HERO_BUTTON_TRAINING, "Обсуждение", HERO_BUTTON_TRAINING_BEFORE_URL)
    safe_click_and_verify(browser, By.XPATH, HERO_BUTTON_TRAINING, "Обсуждение", HERO_BUTTON_TRAINING_AFTER_URL)
    wait_for_page_load(browser) # ждем загрузки страницы
    safe_back_and_verify(browser, BASE_URL_FACT) # возвращаемся назад на главную страницу


    # Проверяем, что кнопка Просмотр кода страницы содержит ссылку на "https://ru.wikipedia.org/w/index.php?title=Заглавная_страница&action=edit"(в sha256)
    safe_find_and_verify_href(browser, By.XPATH, HERO_BUTTON_VIEW_CODE, "Просмотр кода страницы", HERO_BUTTON_VIEW_CODE_BEFORE_URL)
    safe_click_and_verify(browser, By.XPATH, HERO_BUTTON_VIEW_CODE, "Просмотр кода страницы", HERO_BUTTON_VIEW_CODE_AFTER_URL)
    wait_for_page_load(browser) # ждем загрузки страницы
    safe_back_and_verify(browser, BASE_URL_FACT) # возвращаемся назад на главную страницу


    # Проверить, что кнопка История страницы содержит ссылку на "https://ru.wikipedia.org/w/index.php?title=Заглавная_страница&action=history"(в sha256)
    safe_find_and_verify_href(browser, By.XPATH, HERO_BUTTON_HISTORY, "История страницы", HERO_BUTTON_HISTORY_BEFORE_URL)
    safe_click_and_verify(browser, By.XPATH, HERO_BUTTON_HISTORY, "История страницы", HERO_BUTTON_HISTORY_AFTER_URL)
    wait_for_page_load(browser) # ждем загрузки страницы
    safe_back_and_verify(browser, BASE_URL_FACT) # возвращаемся назад на главную страницу


    # Поле поиска сущеcтвует и видно. Плейсхолдер должен быть "Искать в Википедии"
    safe_find_and_verify(browser, By.XPATH, HERO_SEARCH_INPUT, "Поле поиска")
    safe_find_and_verify_placeholder(browser, By.XPATH, HERO_SEARCH_INPUT_SUBCATEGORY, "Плейсхолдер", "Искать в Википедии")


    # Проверяем, что в блоке h1 содержится текст "Добро пожаловать в Википедию,"
    safe_find_and_verify(browser, By.XPATH, HERO_TITLE, "Добро пожаловать в Википедию,")

    # Слово "Википедия" должно быть ссылкой https://ru.wikipedia.org/wiki/Википедия(в sha256)
    safe_find_and_verify_href(browser, By.XPATH, HERO_WIKIPEDIA, "Википедию", HERO_WIKIPEDIA_URL)

    # Кликаем по ссылке "Википедию" и проверяем, что переходим на страницу https://ru.wikipedia.org/wiki/Википедия(в sha256)
    safe_click_and_verify(browser, By.XPATH, HERO_WIKIPEDIA, "Википедию", HERO_WIKIPEDIA_URL)
    wait_for_page_load(browser) # ждем загрузки страницы
    safe_back_and_verify(browser, BASE_URL_FACT) # возвращаемся назад на главную страницу

    # Проверяем, что в параграфе ниже содержится текст "свободную энциклопедию, которую может редактировать каждый."
    safe_find_and_verify(browser, By.XPATH, HERO_PARAGRAPH, "свободную энциклопедию, которую может редактировать каждый.")
    
    # Слово "свободную энциклопедию" должно быть со ссылкой https://ru.wikipedia.org/wiki/Свободный_контент(в sha256)
    safe_find_and_verify_href(browser, By.XPATH, HERO_PARAGRAPH_FREE_CONTENT, "свободную энциклопедию", HERO_FREE_CONTENT_URL)

    # Кликаем по ссылке "свободную энциклопедию" и проверяем, что переходим на страницу https://ru.wikipedia.org/wiki/Свободный_контент(в sha256)
    safe_click_and_verify(browser, By.XPATH, HERO_PARAGRAPH_FREE_CONTENT, "свободную энциклопедию", HERO_FREE_CONTENT_URL)
    wait_for_page_load(browser) # ждем загрузки страницы
    safe_back_and_verify(browser, BASE_URL_FACT) # возвращаемся назад на главную страницу

    # Слово "может редактировать каждый" должно быть со ссылкой https://ru.wikipedia.org/wiki/Справка:Введение_в_Википедию(в sha256)
    safe_find_and_verify_href(browser, By.XPATH, HERO_PARAGRAPH_CAN_EDIT_EVERYONE, "может редактировать каждый", HERO_CAN_EDIT_EVERYONE_URL)

    # Кликаем по ссылке "может редактировать каждый" и проверяем, что переходим на страницу https://ru.wikipedia.org/wiki/Справка:Введение_в_Википедию(в sha256)
    safe_click_and_verify(browser, By.XPATH, HERO_PARAGRAPH_CAN_EDIT_EVERYONE, "может редактировать каждый", HERO_CAN_EDIT_EVERYONE_URL)
    wait_for_page_load(browser) # ждем загрузки страницы
    safe_back_and_verify(browser, BASE_URL_FACT) # возвращаемся назад на главную страницу
