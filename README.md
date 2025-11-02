# wikipedia.org Autotests

Автоматизированные тесты для wikipedia.org.

## Особенности

- **Безопасное тестирование**: Тесты продолжают выполнение даже при ошибках с селекторами
- **Подробное логирование**: Четкие сообщения об успехе/ошибке для каждого элемента
- **Автоматическое ожидание**: Элементы автоматически ожидаются с настраиваемым таймаутом

## Новые безопасные функции

### `safe_find_and_verify(browser, by, selector, element_name, timeout=10)`
Безопасно находит элемент и проверяет его видимость. Если элемент не найден, выводит сообщение об ошибке и продолжает выполнение.

**Пример:**
```python
from functions.check_up import safe_find_and_verify
from selenium.webdriver.common.by import By

# Проверяем элемент HEADER
safe_find_and_verify(browser, By.XPATH, HEADER, "HEADER")
```

### `safe_click_and_verify(browser, by, selector, element_name, expected_url=None, timeout=10)`
Безопасно нажимает на элемент и проверяет результат. Если элемент не найден или не работает, выводит сообщение об ошибке.

**Пример:**
```python
from functions.check_up import safe_click_and_verify

# Кликаем по кнопке и проверяем переход
safe_click_and_verify(browser, By.XPATH, HEADER_BUTTON_REVIEWS, "HEADER_BUTTON_REVIEWS", REVIEWS_URL)
```

## Преимущества нового подхода

1. **Тест не прерывается** при ошибках с селекторами
2. **Подробная информация** о том, что именно не работает
3. **Продолжение выполнения** всех проверок в функции
4. **Четкие сообщения** об успехе/ошибке для каждого элемента
5. **Автоматическое ожидание** элементов с настраиваемым таймаутом

## Установка

```bash
# Windows (PowerShell)
python .\run_tests.py --install
Copy-Item env.example .env

# Windows (cmd)
python run_tests.py --install
copy env.example .env

# Linux / macOS
python3 run_tests.py --install
cp env.example .env
```

## Запуск тестов

```bash
# Запуск всех тестов
python run_tests.py

# Запуск теста Header
python -m pytest tests/ui/landing/test_header.py -v

# Запуск теста Hero
python -m pytest tests/ui/landing/test_hero.py -v

# Запуск всех тестов landing страницы
python -m pytest tests/ui/landing/ -v

# Запуск с HTML-отчётом (предпочтительный способ)
python run_tests.py --report

# Или напрямую через pytest
python -m pytest -v

# С генерацией отчёта напрямую
python -m pytest --html=reports/report.html --self-contained-html


# GIT команды:

# Шаг 0 Создание новой ветки:
git checkout main 
git pull origin main
git checkout -b "Номер задачи"

# Шаг 1: Подготовить изменения к коммиту:
git add .

# Шаг 2: Создать коммит:
git commit -m "Текст коммита"

# Шаг 3: Отправить коммит:
git push origin номер ветки

```

## Установка библиотек 

```bash
# Windows
pip install -r .\requirements.txt

# Linux / macOS
pip install -r requirements.txt
``` 


## Структура проекта

```
autotests/
├── conftest.py                    # Фикстуры pytest
├── requirements.txt               # Зависимости
├── pytest.ini                    # Конфигурация pytest
├── run_tests.py                  # Скрипт запуска
├── config/
│   ├── urls.py                   # URL конфигурация
│   └── elements_and_path/
│       ├── header.py             # Селекторы для блока Header
│       └── hero.py               # Селекторы для блока Hero
├── functions/
│   └── check_up.py               # Вспомогательные функции для тестирования
└── tests/
    └── ui/
        └── landing/
            ├── test_header.py    # Тесты для блока Header
            └── test_hero.py      # Тесты для блока Hero
```

## Тесты

### Landing страница

- `test_header.py` - тесты для проверки блока Header (логотип, кнопки навигации, вход/регистрация)
- `test_hero.py` - тесты для проверки блока Hero (заголовок, параграфы, кнопки действий, поиск)

## HTML отчеты

Проект поддерживает генерацию красивых HTML отчетов с помощью `pytest-html`.

### Генерация отчёта:
```bash
python3 run_tests.py --report
```

### Что содержит отчет:
- ✅ Статистика выполнения тестов
- ✅ Детальная информация по каждому тесту
- ✅ Время выполнения
- ✅ Полные ошибки с трейсбеком
- ✅ Кастомные данные из тестов

### Просмотр отчета:
Откройте файл `reports/report.html` в браузере.

Подробное руководство: [HTML_REPORTS_GUIDE.md](HTML_REPORTS_GUIDE.md)
