"""
Проверка статуса ассерт и вывод лога в отчет (report)
"""

def verify(condition, ok, fail): 
    if condition:
        print(f"✅ {ok}")
        assert condition, ok
        return
    print(f"❌ {fail}")
    assert condition, fail

def safe_find_and_verify(browser, by, selector, element_name, timeout=10):
    """
    Безопасно находит элемент и проверяет его видимость.
    Если элемент не найден, выводит сообщение об ошибке и продолжает выполнение.
    
    Args:
        browser: WebDriver instance
        by: способ поиска (By.XPATH, By.CSS_SELECTOR, etc.)
        selector: селектор для поиска
        element_name: название элемента для вывода в логах
        timeout: время ожидания в секундах
    
    Returns:
        WebElement если найден, None если не найден
    """
    try:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        
        # Ждем появления элемента
        element = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((by, selector))
        )
        
        # Проверяем видимость
        if element.is_displayed():
            print(f"✅ {element_name} найден и виден")
            return element
        else:
            print(f"⚠️ {element_name} найден, но не виден")
            return element
            
    except Exception as e:
        print(f"❌ {element_name} не найден: {str(e)}")
        return None


def safe_find(browser, by, selector, element_name, timeout=10):
    """
    Безопасно находит элемент и проверяет его видимость.
    Если элемент не найден, выводит сообщение об ошибке и продолжает выполнение.
    
    Args:
        browser: WebDriver instance
        by: способ поиска (By.XPATH, By.CSS_SELECTOR, etc.)
        selector: селектор для поиска
        element_name: название элемента для вывода в логах
        timeout: время ожидания в секундах
    
    Returns:
        WebElement если найден, None если не найден
    """
    try:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        
        # Ждем появления элемента
        element = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((by, selector))
        )
        return element
            
    except Exception as e:
        print(f"❌ {element_name} не найден: {str(e)}")
        return None


# проверяем, что элемент существует, виден и содержит текст
def safe_find_and_verify_and_check_text(browser, by, selector, element_name, timeout=10, expected_text=None):
    """
    Безопасно находит элемент и проверяет его видимость и текст.
    Если элемент не найден, выводит сообщение об ошибке и продолжает выполнение.
    Если элемент найден, но текст не соответствует ожидаемому, выводит сообщение об ошибке и продолжает выполнение.
    
    Args:
        browser: WebDriver instance
        by: способ поиска (By.XPATH, By.CSS_SELECTOR, etc.)
        selector: селектор для поиска
        element_name: название элемента для вывода в логах
        timeout: время ожидания в секундах
    
    Returns:
        WebElement если найден, None если не найден
    """
    try:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        
        # Ждем появления элемента
        element = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((by, selector))
        )
        
        # Проверяем видимость
        if element.is_displayed():
            print(f"✅ {element_name} найден и виден")
            
            # Проверяем текст, если он указан
            if expected_text is not None:
                if element.text == expected_text:
                    print(f"✅ {element_name} содержит правильный текст: '{expected_text}'")
                else:
                    print(f"❌ {element_name} содержит неправильный текст. Ожидался: '{expected_text}', получен: '{element.text}'")
            
            return element

        else:
            print(f"⚠️ {element_name} найден, но не виден")
            return element
            
    except Exception as e:
        print(f"❌ {element_name} не найден: {str(e)}")
        return None

def safe_find_and_verify_placeholder(browser, by, selector, element_name, expected_placeholder, timeout=10):
    """
    Находит элемент и проверяет его placeholder атрибут
    """
    try:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        element = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((by, selector))
        )
        
        if element.is_displayed():
            placeholder = element.get_attribute('placeholder')
            if placeholder == expected_placeholder:
                print(f"✅ {element_name} найден с правильным href: {placeholder}")
                return element
            else:
                print(f"❌ {element_name} найден, но href неправильный. Ожидался: {expected_placeholder}, получен: {placeholder}")
                return element
        else:
            print(f"⚠️ {element_name} найден, но не виден")
            return element
            
    except Exception as e:
        print(f"❌ {element_name} не найден: {str(e)}")
        return None


def safe_find_and_verify_href(browser, by, selector, element_name, expected_href, timeout=10):
    """
    Находит элемент и проверяет его href атрибут
    """
    try:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        element = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((by, selector))
        )
        
        if element.is_displayed():
            actual_href = element.get_attribute('href')
            if actual_href == expected_href:
                print(f"✅ {element_name} найден с правильным href: {actual_href}")
                return element
            else:
                print(f"❌ {element_name} найден, но href неправильный. Ожидался: {expected_href}, получен: {actual_href}")
                return element
        else:
            print(f"⚠️ {element_name} найден, но не виден")
            return element
            
    except Exception as e:
        print(f"❌ {element_name} не найден: {str(e)}")
        return None
        

def safe_find_and_verify_not_displayed(browser, by, selector, element_name, timeout=10): # проверяем, что элемент существует, но не виден
    """
    Безопасно находит элемент и проверяет его невидимость.
    Если элемент найден, но не виден - выводит сообщение о том что все хорошо.
    
    Args:
        browser: WebDriver instance
        by: способ поиска (By.XPATH, By.CSS_SELECTOR, etc.)
        selector: селектор для поиска
        element_name: название элемента для вывода в логах
        timeout: время ожидания в секундах
    
    Returns:
        WebElement если найден, None если не найден
    """
    try:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        
        # Ждем появления элемента
        element = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((by, selector))
        )
        
        # Проверяем видимость
        if element.is_displayed():
            print(f"❌ {element_name} найден и виден - плохо")
            return element
        
        elif not element.is_displayed():
            print(f"✅ {element_name} найден, но не виден - все хорошо")
            return element

        else:
            print(f"❌ {element_name} не найден: {str(e)}")
            return None
            
    except Exception as e:
        print(f"❌ {element_name} не найден: {str(e)}")
        return None



def safe_find_and_verify_not_displayed_not_verify(browser, by, selector, element_name, timeout=3): # проверяем, что элемент не существует, и не виден
    """
    Безопасно находит элемент и проверяет его невидимость.
    Если элемент не найден и не виден - выводит сообщение о том что все хорошо.
    
    Args:
        browser: WebDriver instance
        by: способ поиска (By.XPATH, By.CSS_SELECTOR, etc.)
        selector: селектор для поиска
        element_name: название элемента для вывода в логах
        timeout: время ожидания в секундах
    
    Returns:
        WebElement если найден, None если не найден
    """
    try:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        
        # Ждем появления элемента
        element = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((by, selector))
        )
        
        # Проверяем видимость
        if element.is_displayed():
            print(f"❌ {element_name} найден и виден - плохо")
            return element
        
        elif not element.is_displayed():
            print(f"✅ {element_name} найден, но не виден - все хорошо")
            return element

        else:
            print(f"❌ {element_name} не найден: {str(e)}")
            return None
            
    except Exception as e:
        print(f"✅ {element_name} не существует - все хорошо")
        return None



def safe_click_and_verify(browser, by, selector, element_name, expected_url=None, timeout=10):
    """
    Безопасно нажимает на элемент и проверяет результат.
    Если элемент не найден или не работает, выводит сообщение об ошибке.
    
    Args:
        browser: WebDriver instance
        by: способ поиска
        selector: селектор для поиска
        element_name: название элемента
        expected_url: ожидаемый URL после клика (опционально)
        timeout: время ожидания
    
    Returns:
        bool: True если операция успешна, False если произошла ошибка
    """
    try:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        element = safe_find_and_verify(browser, by, selector, element_name, timeout)
        if element is None:
            return False
            
        # Кликаем по элементу
        element.click()
        print(f"✅ Клик по {element_name} выполнен")
        
        # Если указан ожидаемый URL, проверяем его
        if expected_url:
            try:
                WebDriverWait(browser, timeout).until(EC.url_to_be(expected_url))
                print(f"✅ Переход на {expected_url} выполнен успешно")
                return True
            except Exception as e:
                print(f"❌ Переход на {expected_url} не выполнен: {str(e)}")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка при клике по {element_name}: {str(e)}")
        return False


def safe_click_and_verify_contains(browser, by, selector, element_name, expected_url=None, timeout=10): # нажимаем на элемент и проверяем, что в URL содержится ожидаемый URL
    """
    Безопасно нажимает на элемент и проверяет результат.
    Если элемент не найден или не работает, выводит сообщение об ошибке.
    
    Args:
        browser: WebDriver instance
        by: способ поиска
        selector: селектор для поиска
        element_name: название элемента
        expected_url: ожидаемый URL после клика (опционально)
        timeout: время ожидания
    
    Returns:
        bool: True если операция успешна, False если произошла ошибка
    """
    try:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.common.exceptions import TimeoutException
        
        element = safe_find_and_verify(browser, by, selector, element_name, timeout)
        if element is None:
            return False
            
        # Кликаем по элементу
        element.click()
        print(f"✅ Клик по {element_name} выполнен")

        if len(browser.window_handles) > 1:
            browser.switch_to.window(browser.window_handles[-1]) # Переключаемся на последнюю вкладку
        
        # Если указан ожидаемый URL, проверяем его
        if expected_url:
            
            browser.set_page_load_timeout(3) 
            
            try:
                
                WebDriverWait(browser, timeout).until(EC.url_contains(expected_url))
                print(f"✅ Переход на {expected_url} выполнен успешно")
                return True

            except TimeoutException as e:
                browser.execute_script("window.stop();")
                
                try:
                    WebDriverWait(browser, timeout).until(EC.url_contains(expected_url))
                    print(f"✅ Переход на {expected_url} выполнен успешно после прерывания")
                    return True
                except Exception as e2:
                    print(f"❌ Переход на {expected_url} не выполнен даже после прерывания: {str(e2)}")
                    return False

            except Exception as e:
                print(f"❌ Переход на {expected_url} не выполнен: {str(e)}")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка при клике по {element_name}: {str(e)}")
        return False


def scroll_to_element(browser, by, selector, element_name, timeout=10):
    """
    Скроллит к элементу и делает его видимым.
    
    Args:
        browser: WebDriver instance
        by: способ поиска
        selector: селектор для поиска
        element_name: название элемента
        timeout: время ожидания
    
    Returns:
        WebElement если найден, None если не найден
    """
    try:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        element = safe_find(browser, by, selector, element_name, timeout)
        if element is None:
            return None
        
        # Получаем начальную позицию
        start_position = browser.execute_script("return window.pageYOffset;")

        # Скроллим к элементу
        browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        
        # Ждем изменения позиции
        WebDriverWait(browser, 5).until(
            lambda driver: driver.execute_script("return window.pageYOffset;") != start_position
        )

        print(f"✅ Скролл к {element_name} выполнен") 
        return element
        
    except Exception as e:
        print(f"❌ Ошибка при скролле к {element_name}: {str(e)}")
        return None


def scroll_down(browser, pixels=500):
    """
    Скроллит страницу вниз на указанное количество пикселей.
    
    Args:
        browser: WebDriver instance
        pixels: количество пикселей для скролла (по умолчанию 500)
    """
    try:
        from selenium.webdriver.support.ui import WebDriverWait
        # Получаем начальную позицию
        start_position = browser.execute_script("return window.pageYOffset;")
        
        # Выполняем скролл
        browser.execute_script(f"window.scrollBy(0, {pixels});")
        
        # Ждем изменения позиции
        WebDriverWait(browser, 5).until(
            lambda driver: driver.execute_script("return window.pageYOffset;") != start_position
        )

        print(f"✅ Скролл вниз на {pixels}px выполнен")

    except Exception as e:
        print(f"❌ Ошибка при скролле вниз: {str(e)}")


def scroll_to_bottom(browser):
    """
    Скроллит страницу до самого низа.
    """
    try:
        import time
        from selenium.webdriver.support.ui import WebDriverWait

        # Получаем начальную позицию
        start_position = browser.execute_script("return window.pageYOffset;")

        # Выполняем скролл
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Ждем изменения позиции
        WebDriverWait(browser, 5).until(
            lambda driver: driver.execute_script("return window.pageYOffset;") != start_position
        )

        print("✅ Скролл до низа страницы выполнен")
        
        time.sleep(0.5) # пауза на 0.5 секунды

    except Exception as e:
        print(f"❌ Ошибка при скролле до низа: {str(e)}")


def scroll_to_top(browser):
    """
    Скроллит страницу до самого верха.
    """
    try:
        import time
        from selenium.webdriver.support.ui import WebDriverWait

        # Получаем начальную позицию
        start_position = browser.execute_script("return window.pageYOffset;")

        # Выполняем скролл
        browser.execute_script("window.scrollTo(0, 0);")

        # Ждем изменения позиции
        WebDriverWait(browser, 5).until(
            lambda driver: driver.execute_script("return window.pageYOffset;") != start_position
        )

        print("✅ Скролл до верха страницы выполнен")

        time.sleep(0.5) # пауза на 0.5 секунды

    except Exception as e:
        print(f"❌ Ошибка при скролле до верха: {str(e)}")


def smooth_scroll_down(browser, steps=5, delay=0.1):
    """
    Плавный скролл вниз с несколькими шагами (имитирует человеческое поведение).
    
    Args:
        browser: WebDriver instance
        steps: количество шагов скролла
        delay: задержка между шагами в секундах
    """
    try:
        import time
        
        # Получаем высоту страницы
        page_height = browser.execute_script("return document.body.scrollHeight")
        scroll_step = page_height // steps
        
        for i in range(steps):
            browser.execute_script(f"window.scrollBy(0, {scroll_step});")
            time.sleep(delay)
            
        print(f"✅ Плавный скролл вниз выполнен ({steps} шагов)")
    except Exception as e:
        print(f"❌ Ошибка при плавном скролле: {str(e)}")




def wait_for_page_load(browser, timeout=10):
    """Ждет загрузки страницы"""
    try:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.common.by import By
        
        WebDriverWait(browser, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        
    except Exception as e:
        print(f"❌ Страница не загружена: {str(e)}")
        return False


def safe_back_and_verify(browser, expected_url=None, timeout=10):
    """
    Безопасно переходит назад в браузере и проверяет URL.
    
    Args:
        browser: WebDriver instance
        expected_url: ожидаемый URL после перехода назад (опционально)
        timeout: время ожидания загрузки страницы
    
    Returns:
        bool: True если переход успешен, False если произошла ошибка
    """
    try:
        # Запоминаем текущий URL
        current_url = browser.current_url
        
        # Переходим назад
        browser.back() 

        # Ждем загрузки страницы
        wait_for_page_load(browser, timeout)
        
        # Получаем новый URL
        new_url = browser.current_url
        
        # Проверяем, что URL изменился
        if current_url != new_url:
                        
            # Если указан ожидаемый URL, проверяем его
            if expected_url:
                if new_url == expected_url:
                    print(f"✅ Переход назад на {expected_url} выполнен")
                    return True
                else:
                    print(f"❌ Переход назад не на ожидаемую страницу. Ожидался: {expected_url}, получен: {new_url}")
                    return False
            else:
                print(f"✅ Переход назад выполнен: {new_url}")
                return True
        else:
            print("❌ Переход назад не выполнен - URL не изменился")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка при переходе назад: {str(e)}")
        return False


def close_window_and_back_to_main_window(browser):
    """
    Закрывает текущую вкладку и переключается на главную вкладку.
    """
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    browser.implicitly_wait(0.5)


def wait_for_text_in_xpath(browser, xpath, expected_text, timeout=10):
    """
    Ждет появления нужного текста в элементе по XPath.
    
    Args:
        browser: WebDriver instance
        xpath: XPath селектор
        expected_text: ожидаемый текст
        timeout: время ожидания в секундах
    
    Returns:
        bool: True если текст найден, False если не найден
    """
    try:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        
        WebDriverWait(browser, timeout).until(
            EC.text_to_be_present_in_element((By.XPATH, xpath), expected_text)
        )
        print(f"✅ Текст '{expected_text}' найден в элементе")
        return True
        
    except Exception as e:
        print(f"❌ Текст '{expected_text}' не найден: {str(e)}")
        return False