import time

import allure
import pytest_check as check
from locators.locators_enter_in_avby import EnterPage
from conftest import web_browser


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_enter_on(web_browser):
    """Этот тест проверяет страницу входа"""

    page = EnterPage(web_browser)

    element_text = [
                    (page.text_enter, 'Вход'),
                    (page.text_phone, 'Телефон'),
                    (page.text_on_password, 'Пароль'),
                    (page.btn_no_remember_password, 'Не помню пароль'),
                    (page.btn_enter, 'Войти'),
                    (page.text_registration, 'Регистрация'),
                    (page.text_registration_under, 'для тех, кто первый раз на сайте'),
                    (page.tab_email_and_login, 'почте или логину'),
                    (page.tab_phone, 'по телефону'),
                    ]

    with allure.step('Проверка, что кнопка Вход есть на экране'):
        check.is_true(page.btn_enter_in.is_visible())

    with allure.step('Проверка, что кнопка Вход кликабельна'):
        check.is_true(page.btn_enter_in.is_clickable())

    with allure.step('Проверка, орфографии'):
        check.equal(page.btn_enter_in.get_text(), "Войти")

    with allure.step('Нажимаем на кнопку'):
        page.btn_enter_in.click()

    with allure.step('Проверка, открылась ли панель'):
        time.sleep(1)
        check.is_true(page.panel_enter.is_visible())

    for element, text_element in element_text:
        with allure.step('Проверка, орфографии'):
            check.equal(element.get_text(), text_element)

    with allure.step('Проверка, что все элементы кликабельны'):
        check.is_false(page.btn_enter.is_clickable())
        check.is_true(page.btn_no_remember_password.is_clickable())
        check.is_true(page.btn_registration.is_clickable())
        check.is_true(page.eyes_on_password.is_clickable())
        check.is_true(page.btn_no_remember_password.is_clickable())
        check.is_true(page.tab_email_and_login.is_clickable())
        check.is_true(page.tab_phone.is_clickable())


    with allure.step('Ввод телефона'):
        page.input_phone.send_keys('298593261')

    with allure.step('Ввод пароля'):
        page.input_password.send_keys('qaartemijtester1110')

    with allure.step('Нажать на кнопку "Войти"'):
        page.btn_enter.click()
        time.sleep(3)





