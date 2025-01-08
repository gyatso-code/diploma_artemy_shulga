import time

import allure
import pytest_check as check
from locators.locators_header_page import HeaderPage
from conftest import web_browser

@allure.story('Тест главной страницы "av.by"')
@allure.feature('Проверка хедера')
def test_headers_main(web_browser):
    """ Этот тест проверяет кликабельность элементов хедера, их наличие и корректность переходов по ссылкам """

    page = HeaderPage(web_browser)

    elements = [(page.btn_menu_header_announcement, 'Объявления', 'https://cars.av.by/'),
                (page.btn_menu_header_services, 'Сервисы', 'https://av.by/vin'),
                (page.btn_menu_header_magazine, 'Журнал', 'https://av.by/news'),
                (page.btn_menu_header_knowledge, 'Знания', 'https://av.by/pages/info'),
                (page.btn_menu_header_attendance, 'Услуги', 'https://av.by/company'),
                (page.btn_menu_header_vin_check, 'Проверка VIN', 'https://av.by/vin')]

    elements_user = [(page.btn_menu_header_login, 'Войти'),
                     (page.btn_menu_header_place_an_ad, 'Подать объявление')]

    page.btn_passed_cookie.click()
    time.sleep(3)

    for element, text_element, url_elements in elements:
        with allure.step(f"Проверка элемента хедера: {text_element}"):
            element.click()
            check.equal(page.get_current_url(), url_elements, "URL не совпадает")
            check.is_true(element.is_clickable(), "Элемент не кликабелен")
            check.is_true(element.is_visible(), "Элемент не виден")
            check.equal(element.get_text(), text_element, "Текст элемента некорректен")
            check.equal(element.get_attribute('href'), url_elements, "Ссылка некорректна")

    for buttons, text_buttons in elements_user:
        with allure.step(f"Проверка кнопки хедера: {text_buttons}"):
            check.is_true(buttons.is_clickable(), "Кнопка не кликабельна")
            check.is_true(buttons.is_visible(), "Кнопка не видна")
            check.equal(buttons.get_text(), text_buttons, "Текст кнопки некорректен")
