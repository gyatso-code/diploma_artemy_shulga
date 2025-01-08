import time

import allure
import pytest_check as check
from locators.locators_authorization_page import AuthorizationPage
from conftest import web_browser


@allure.story('Тест авторизации на "av.by"')
@allure.feature('Тест для проверки входа по номеру телефона')
def test_enter_phone(web_browser):
    """ Этот тест проверяет кликабельность элементов на странице входа по номеру телефона,
     их наличие и корректность, вход на сайт"""

    page = AuthorizationPage(web_browser)

    page.btn_passed_cookie.click()
    time.sleep(3)

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

    with allure.step("Тест проверки -- кнопка 'Вход' есть на экране"):
        check.is_true(page.btn_enter_in.is_visible(), "Кнопка 'Вход' не отображается")

    with allure.step("Тест проверки -- кнопка 'Вход' кликабельна"):
        check.is_true(page.btn_enter_in.is_clickable(), "Кнопка 'Вход' не кликабельна")

    with allure.step("Проверка текста на кнопке 'Вход'"):
        check.equal(page.btn_enter_in.get_text(), "Войти", "Текст кнопки 'Вход' некорректен")

    with allure.step("Нажимаем на кнопку 'Вход'"):
        page.btn_enter_in.click()

    with allure.step("Тест проверки -- открылась ли панель входа"):
        time.sleep(1)
        check.is_true(page.panel_enter.is_visible(), "Панель входа не открылась")

    for element, text_element in element_text:
        with allure.step(f"Проверка текста элемента: {text_element}"):
            check.equal(element.get_text(), text_element, f"Текст элемента '{element.get_text()}' некорректен")

    with allure.step("Тест проверки -- все элементы в панели кликабельны"):
        check.is_false(page.btn_enter.is_clickable(), "Кнопка 'Войти' должна быть неактивной")
        check.is_true(page.btn_no_remember_password.is_clickable(), "'Не помню пароль' не кликабельна")
        check.is_true(page.btn_registration.is_clickable(), "'Регистрация' не кликабельна")
        check.is_true(page.btn_eyes_on_password.is_clickable(), "Иконка показа пароля не кликабельна")
        check.is_true(page.tab_email_and_login.is_clickable(), "Вкладка 'почте или логину' не кликабельна")
        check.is_true(page.tab_phone.is_clickable(), "Вкладка 'по телефону' не кликабельна")
        check.is_true(page.btn_close.is_visible(),  "Кнопка закрытия панели не отображается")

    with allure.step("Тест проверки -- ввод в поле 'Телефон'"):
        page.input_phone_and_email.send_keys('298593261')

    with allure.step("Тест проверки -- ввод в поле 'Пароль'"):
        page.input_password.send_keys('qaartemijtester1110')

    with allure.step("Тест проверки -- нажатие на кнопку 'Войти"):
        page.btn_enter.click()
        time.sleep(3)

    with allure.step("Тест проверки -- вошел ли пользователь в аккаунт"):
        check.is_true(page.btn_logo_user.is_visible(), "Пользователь не вошел в аккаунт")


@allure.feature('Тест для проверки входа по электронной почте или логину')
def test_enter_email_or_login(web_browser):
    """ Этот тест проверяет кликабельность элементов на странице входа по электронной почте или логину,
     их наличие и корректность, вход на сайт"""

    page = AuthorizationPage(web_browser)

    page.btn_passed_cookie.click()
    time.sleep(3)

    element_text = [
        (page.text_email_or_login, 'Электронная почта или логин'),
        (page.text_on_password, 'Пароль'),
        (page.btn_no_remember_password, 'Не помню пароль'),
        (page.btn_enter, 'Войти'),
        (page.text_registration, 'Регистрация'),
        (page.text_registration_under, 'для тех, кто первый раз на сайте'),
    ]

    page.btn_enter_in.click()
    time.sleep(1)

    page.tab_email_and_login.click()
    time.sleep(1)

    with allure.step("Тест проверки -- все элементы в панели кликабельны"):
        check.is_false(page.btn_enter.is_clickable(), "Кнопка 'Войти' должна быть неактивной")
        check.is_true(page.btn_no_remember_password.is_clickable(), "'Не помню пароль' не кликабельна")
        check.is_true(page.btn_registration.is_clickable(), "'Регистрация' не кликабельна")
        check.is_true(page.btn_eyes_on_password.is_clickable(), "Иконка показа пароля не кликабельна")

    for element, text_element in element_text:
        with allure.step(f"Проверка текста элемента: {text_element}"):
            check.equal(element.get_text(), text_element, f"Текст элемента '{element.get_text()}' некорректен")

    with allure.step("Тест проверки -- ввод в поле 'Электронная почта или логин'"):
        page.input_phone_and_email.send_keys('art.pointqa@gmail.com')

    with allure.step("Тест проверки -- ввод в поле 'Пароль'"):
        page.input_password.send_keys('qaartemijtester1110')

    with allure.step("Тест проверки -- нажатие на кнопку 'Войти"):
        page.btn_enter.click()
        time.sleep(3)

    with allure.step("Тест проверки -- пользователь вошел в аккаунт"):
        check.is_true(page.btn_logo_user.is_visible(), "Пользователь не вошел в аккаунт")