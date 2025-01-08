import time

import string
import random
import allure
import pytest_check as check
from locators.locators_registration_page import RegistrationPage
from conftest import web_browser



@allure.story('Тест регистрации на "av.by"')
@allure.feature('Тест для проверки страницы регистрации по телефону')
def test_register_phone(web_browser):
    """ Этот тест проверяет кликабельность элементов на странице регистрации по телефону,
     их наличие и корректность, подтверждение"""

    page = RegistrationPage(web_browser)

    page.btn_passed_cookie.click()
    time.sleep(3)

    page.btn_enter_in.click()
    time.sleep(1)

    page.btn_registration.click()
    time.sleep(1)

    with allure.step("Тест проверки -- все элементы в панели кликабельны"):
        check.is_true(page.tab_email_register.is_clickable(), "Вкладка 'почте' не кликабельна")
        check.is_true(page.tab_phone_register.is_clickable(), "Вкладка 'по телефону' не кликабельна")
        check.is_false(page.btn_register_menu.is_clickable(), "Кнопка 'Зарегистрироваться' должна быть неактивной")
        check.is_true(page.btn_enter_register_menu.is_clickable(), "'Вход' не кликабельна")
        check.is_true(page.btn_eyes_on_password.is_clickable(), "Иконка показа пароля не кликабельна")

    element_text = [
        (page.text_registration_menu, 'Регистрация'),
        (page.text_name_on_cyr, 'Имя на кириллице'),
        (page.text_phone_register, 'Телефон'),
        (page.text_on_password_register, 'Пароль'),
        (page.btn_register_menu, 'Зарегистрироваться'),
        (page.text_enter_menu_register, 'Вход'),
        (page.text_enter_menu_register_under, 'для тех, кто уже зарегистрирован'),
        (page.tab_email_register, 'почте'),
        (page.tab_phone_register, 'по телефону'),
        (page.text_info_user, 'Не короче 8 символов и только латиница и цифры'),
    ]

    for element, text_element in element_text:
        with allure.step(f"Проверка текста элемента: {text_element}"):
            check.equal(element.get_text(), text_element, f"Текст элемента '{element.get_text()}' некорректен")

    with allure.step("Тест проверки -- ввод в поле 'Имя на кириллице'"):
        page.input_user_name_register.send_keys('Василий')

    with allure.step("Тест проверки -- ввод в поле 'Телефон'"):
        page.input_phone_register.send_keys('298323232')

    with allure.step("Тест проверки -- ввод в поле 'Пароль'"):
        page.input_password_register.send_keys('dDR543TGfghd')

    with allure.step("Тест проверки -- нажатие на кнопку 'Зарегистрироваться"):
        page.btn_register_menu.click()
        time.sleep(1)

    with allure.step("Тест проверки -- на отображение текста 'Подтверждение номера телефона'"):
        check.is_true(page.text_passes_phone.is_visible(), "Подтверждение отсутствует")


def generate_random_email(domain="gmail.com", length=8):
    """ Генератор случайный email """
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{username}@{domain}"


@allure.feature('Тест для проверки страницы регистрации по почте')
def test_register_email(web_browser):
    """ Этот тест проверяет кликабельность элементов на странице регистрации по почте,
     их наличие и корректность, подтверждение"""

    page = RegistrationPage(web_browser)

    page.btn_passed_cookie.click()
    time.sleep(3)

    page.btn_enter_in.click()
    time.sleep(1)

    page.btn_registration.click()
    time.sleep(1)

    page.tab_email_register.click()
    time.sleep(1)

    random_email = generate_random_email()

    with allure.step("Тест проверки -- все элементы в панели кликабельны"):
        check.is_false(page.btn_register_menu.is_clickable(), "Кнопка 'Зарегистрироваться' должна быть неактивной")
        check.is_true(page.btn_enter_register_menu.is_clickable(), "'Вход' не кликабельна")
        check.is_true(page.btn_eyes_on_password_email.is_clickable(), "Иконка показа пароля не кликабельна")

    element_text = [
        (page.text_registration_menu, 'Регистрация'),
        (page.text_name_email_cyr, 'Имя на кириллице'),
        (page.text_email_register_email, 'Электронная почта'),
        (page.text_password_email, 'Пароль'),
        (page.btn_register_email, 'Зарегистрироваться'),
        (page.text_enter_menu_register, 'Вход'),
        (page.text_enter_menu_register_under, 'для тех, кто уже зарегистрирован'),
        (page.tab_email_register, 'почте'),
        (page.tab_phone_register, 'по телефону'),
        (page.text_info_user_email, 'Не короче 8 символов и только латиница и цифры')
    ]

    for element, text_element in element_text:
        with allure.step(f"Проверка текста элемента: {text_element}"):
            check.equal(element.get_text(), text_element, f"Текст элемента '{element.get_text()}' некорректен")

    with allure.step("Тест проверки -- ввод в поле 'Имя на кириллице'"):
        page.input_user_name_register_email.send_keys('Артемий')

    with allure.step("Тест проверки -- ввод в поле 'Электронная почта'"):
        page.input_email.send_keys(random_email)

    with allure.step("Тест проверки -- ввод в поле 'Пароль'"):
        page.input_password_register_email.send_keys('SDFDeffgt54')

    page.btn_register_email.click()
    time.sleep(1)

    with allure.step("Тест проверки -- на отображение текста 'Подтверждение почтового адреса'"):
        check.is_true(page.text_passes_email.is_visible(), "Подтверждение отсутствует")
