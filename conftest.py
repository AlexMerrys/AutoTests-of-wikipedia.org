"""
Основной файл конфигурации pytest для проекта Википедия
Содержит общие фикстуры и настройки для всех тестов
"""

import os
from queue import Full
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Загружаем переменные окружения из .env файла
load_dotenv()


@pytest.fixture(scope="function")
def browser():
    """Фикстура для запуска браузера"""
    browser_name = os.getenv("BROWSER", "chrome").lower()
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    
    if browser_name == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        # Дополнительно фиксируем размер окна на случай, если аргумент не применился
        try:
            driver.set_window_size(Full)
        except Exception:
            pass
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")
    
    # Устанавливаем неявное ожидание
    implicit_wait = int(os.getenv("IMPLICIT_WAIT", "10"))
    driver.implicitly_wait(implicit_wait)
    
    yield driver
    
    # Закрываем браузер после теста
    driver.quit()
