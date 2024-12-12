import time

import allure
import pytest_check as check
from locators.locators_header_page_avby import HeaderPage
from conftest import web_browser

@allure.story('Тест главной страницы "av.by"')
@allure.feature('Проверка хедера')
def test_headers_main(web_browser):
    """Этот тест проверяет кликабельность, наличие элементов, провописание """

    page = HeaderPage(web_browser)

    elements = [(page.btn_menu_header_announcement, 'Объявления', 'https://cars.av.by/'),
                (page.btn_menu_header_services, 'Сервисы', 'https://av.by/vin'),
                (page.btn_menu_header_magazine, 'Журнал', 'https://av.by/news'),
                (page.btn_menu_header_knowledge, 'Знания', 'https://av.by/pages/info'),
                (page.btn_menu_header_attendance, 'Услуги', 'https://av.by/company'),
                (page.btn_menu_header_vin_check, 'Проверка VIN', 'https://av.by/vin'),
                ]

    for element, text_element, url_elements in elements:
        with allure.step('Тест проверки правильного URL при переходе'):
            element.click()
            check.equal(page.get_current_url(), url_elements)

        with allure.step("Проверка кликабельности"):
            check.is_true(element.is_clickable())

        with allure.step("Проверка на наличие на экране элементов"):
            check.is_true(element.is_visible())

        with allure.step("Проверка орфографии"):
            check.equal(element.get_text(), text_element)

        with allure.step("Тест проверки на правильный адрес кнопки"):
            check.equal(element.get_attribute('href'), url_elements)



