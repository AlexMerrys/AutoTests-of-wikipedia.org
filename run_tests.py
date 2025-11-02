#!/usr/bin/env python3
"""
Скрипт для запуска автотестов wikipedia.org
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


def run_command(command, description=""):
    """Выполняет команду и выводит результат"""
    print(f"\n{'='*50}")
    if description:
        print(f"🚀 {description}")
    print(f"Команда: {command}")
    print(f"{'='*50}\n")
    
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"\n✅ {description} завершено успешно!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Ошибка при выполнении: {e}")
        return False


def check_environment():
    """Проверяет наличие необходимых файлов и зависимостей"""
    print("🔍 Проверка окружения...")
    
    # Проверяем наличие .env файла
    if not os.path.exists(".env"):
        print("⚠️  Файл .env не найден!")
        print("📝 Создайте файл .env на основе env.example:")
        if os.name == "nt":
            print("   copy env.example .env   (PowerShell: Copy-Item env.example .env)")
        else:
            print("   cp env.example .env")
        return False
    
    # Проверяем наличие requirements.txt
    if not os.path.exists("requirements.txt"):
        print("❌ Файл requirements.txt не найден!")
        return False
    
    # Проверяем установку зависимостей
    try:
        import pytest
        import selenium
        print("✅ Все зависимости установлены")
    except ImportError as e:
        print(f"❌ Отсутствуют зависимости: {e}")
        print("📦 Установите зависимости: pip install -r requirements.txt")
        return False
    
    return True


def main():
    parser = argparse.ArgumentParser(description="Запуск автотестов PARTYstation")
    parser.add_argument("--install", action="store_true", help="Установить зависимости")
    parser.add_argument("--check", action="store_true", help="Только проверить окружение")
    parser.add_argument("--report", action="store_true", help="Генерировать HTML отчет")
    
    args = parser.parse_args()
    
    # Установка зависимостей
    if args.install:
        print("📦 Установка зависимостей...")
        run_command("pip install -r requirements.txt", "Установка зависимостей")
        return
    
    # Проверка окружения
    if args.check:
        check_environment()
        return
    if not check_environment():
        return
    
    # Формируем команду pytest
    cmd_parts = ["python3", "-m", "pytest", "-v", "--disable-warnings"] # ПОМЕНЯТЬ НА python3 ЕСЛИ НА МАКЕ
    
    # Добавляем генерацию отчета
    if args.report:
        # Создаем папку reports если её нет
        Path("reports").mkdir(exist_ok=True)
        cmd_parts.extend(["--html=reports/report.html", "--self-contained-html"])
    
    # Формируем финальную команду
    command = " ".join(cmd_parts)
    
    # Запускаем тесты
    success = run_command(command, "Запуск тестов")
    
    if success:
        print("\n🎉 Тесты выполнены успешно!")
    else:
        print("\n💥 Тесты завершились с ошибками!")
        sys.exit(1)


if __name__ == "__main__":
    main()
