#!/bin/bash

# Получаем текущую директорию скрипта
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

# Определяем путь к тестовому файлу относительно директории со скриптом
# shellcheck disable=SC2034
TEST_FILE="$SCRIPT_DIR/../tests/test_footer_page_avby.py"

# Определяем путь к директории с отчетами относительно директории со скриптом
REPORT_DIR="$SCRIPT_DIR/../reports"

# Запускаем pytest с использованием относительного пути к файлу test_my_project.py и директории с отчетами
pytest -v -s "$TEST_FILE" --alluredir="$REPORT_DIR"
