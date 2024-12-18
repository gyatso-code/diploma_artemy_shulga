#!/bin/bash

# Получаем текущую директорию скрипта
SCRIPT_DIR=$(dirname "$0")

# Определяем путь к тестовому файлу относительно директории со скриптом
TEST_FILE_ONE="$SCRIPT_DIR/../tests/test_header_page_avby.py"
TEST_FILE_TWO="$SCRIPT_DIR/../tests/test_footer_page_avby.py"
TEST_FILE_THREE="$SCRIPT_DIR/../tests/test_list_of_cars_avby.py"
TEST_FILE_FOUR="$SCRIPT_DIR/../tests/test_registration_avby.py"
TEST_FILE_FIVE="$SCRIPT_DIR/../tests/test_main_page_avby.py"

# Определяем путь к директории с отчетами относительно директории со скриптом
REPORT_DIR="$SCRIPT_DIR/../reports"

# Запускаем pytest с использованием относительного пути к файлу test_my_project.py и директории с отчетами
pytest -v -s "TEST_FILE_ONE" --alluredir="$REPORT_DIR"
pytest -v -s "TEST_FILE_TWO" --alluredir="$REPORT_DIR"
pytest -v -s "TEST_FILE_THREE" --alluredir="$REPORT_DIR"
pytest -v -s "TEST_FILE_FIVE" --alluredir="$REPORT_DIR"