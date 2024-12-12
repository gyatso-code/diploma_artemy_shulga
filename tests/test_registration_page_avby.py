import time

import string
import random
import allure
import pytest_check as check
from locators.locators_registration_avby import RegistrationPage
from conftest import web_browser


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки страницу входа по номеру телефона')
def test_enter_phone(web_browser):
    """Этот тест проверяет страницу входа"""

    page = RegistrationPage(web_browser)

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

    with allure.step("Тест проверки -- кнопка Вход есть на экране"):
        check.is_true(page.btn_enter_in.is_visible())

    with allure.step("Тест проверки -- кнопка Вход кликабельна"):
        check.is_true(page.btn_enter_in.is_clickable())

    with allure.step("Проверка орфографии"):
        check.equal(page.btn_enter_in.get_text(), "Войти")

    with allure.step('Нажимаем на кнопку'):
        page.btn_enter_in.click()

    with allure.step("Тест проверки -- открылась ли панель"):
        time.sleep(1)
        check.is_true(page.panel_enter.is_visible())

    for element, text_element in element_text:
        with allure.step("Проверка орфографии"):
            check.equal(element.get_text(), text_element)

    with allure.step("Тест проверки -- все элементы в панели кликабельны"):
        check.is_false(page.btn_enter.is_clickable())
        check.is_true(page.btn_no_remember_password.is_clickable())
        check.is_true(page.btn_registration.is_clickable())
        check.is_true(page.btn_eyes_on_password.is_clickable())
        check.is_true(page.tab_email_and_login.is_clickable())
        check.is_true(page.tab_phone.is_clickable())
        check.is_true(page.btn_close.is_visible())

    with allure.step("Тест проверки -- ввод в поле 'Телефон'"):
        page.input_phone_and_email.send_keys('298593261')

    with allure.step("Тест проверки -- ввод в поле 'Пароль'"):
        page.input_password.send_keys('qaartemijtester1110')

    with allure.step("Тест проверки -- нажатие на кнопку 'Войти"):
        page.btn_enter.click()
        time.sleep(3)

    with allure.step("Тест проверки -- вошел ли пользователь в аккаунт"):
        check.is_true(page.btn_logo_user.is_visible())


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки страницу входа по электронной почте')
def test_enter_email_or_login(web_browser):

    page = RegistrationPage(web_browser)

    element_text = [
        (page.text_enter, 'Вход'),
        (page.text_email_or_login, 'Электронная почта или логин'),
        (page.text_on_password, 'Пароль'),
        (page.btn_no_remember_password, 'Не помню пароль'),
        (page.btn_enter, 'Войти'),
        (page.text_registration, 'Регистрация'),
        (page.text_registration_under, 'для тех, кто первый раз на сайте'),
        (page.tab_email_and_login, 'почте или логину'),
        (page.tab_phone, 'по телефону'),
    ]

    page.btn_enter_in.click()
    time.sleep(1)

    page.tab_email_and_login.click()
    time.sleep(1)

    with allure.step("Тест проверки -- все элементы в панели кликабельны"):
        check.is_false(page.btn_enter.is_clickable())
        check.is_true(page.btn_no_remember_password.is_clickable())
        check.is_true(page.btn_registration.is_clickable())
        check.is_true(page.btn_eyes_on_password.is_clickable())
        check.is_true(page.tab_email_and_login.is_clickable())
        check.is_true(page.tab_phone.is_clickable())
        check.is_true(page.btn_close.is_visible())

    for element, text_element in element_text:
        with allure.step("Проверка орфографии"):
            check.equal(element.get_text(), text_element)

    with allure.step("Тест проверки -- ввод в поле 'Электронная почта или логин'"):
        page.input_phone_and_email.send_keys('art.pointqa@gmail.com')

    with allure.step("Тест проверки -- ввод в поле 'Пароль'"):
        page.input_password.send_keys('qaartemijtester1110')

    with allure.step("Тест проверки -- нажатие на кнопку 'Войти"):
        page.btn_enter.click()
        time.sleep(3)

    with allure.step("Тест проверки -- пользователь вошел в аккаунт"):
        check.is_true(page.btn_logo_user.is_visible())


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки страницы регистрации по телефону')
def test_register_phone(web_browser):

    page = RegistrationPage(web_browser)

    page.btn_enter_in.click()
    time.sleep(1)

    page.btn_registration.click()
    time.sleep(1)

    with allure.step("Тест проверки -- все элементы в панели кликабельны"):
        check.is_true(page.tab_email_register.is_clickable())
        check.is_true(page.tab_phone_register.is_clickable())
        check.is_false(page.btn_register_menu.is_clickable())
        check.is_true(page.btn_enter_register_menu.is_clickable())
        check.is_true(page.btn_eyes_on_password.is_clickable())
        check.is_true(page.btn_close.is_visible())

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
        with allure.step("Проверка орфографии"):
            check.equal(element.get_text(), text_element)

    with allure.step("Тест проверки -- ввод в поле 'Имя на кириллице'"):
        page.input_user_name_register.send_keys('Василий')

    with allure.step("Тест проверки -- ввод в поле 'Телефон'"):
        page.input_phone_register.send_keys('298323232')

    with allure.step("Тест проверки -- ввод в поле 'Пароль'"):
        page.input_password_register.send_keys('dDR543TGfghd')

    with allure.step("Тест проверки -- нажатие на кнопку 'Зарегистрироваться"):
        page.btn_register_menu.click()
        time.sleep(5)

    with allure.step("Тест проверки -- на отображение текста 'Подтверждение номера телефона'"):
        page.text_passes_phone.is_visible()
        time.sleep(1)


def generate_random_email(domain="gmail.com", length=8):
    """ Генератор случайный email """
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{username}@{domain}"


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки страницы регистрации по электронной почте')
def test_register_email(web_browser):

    page = RegistrationPage(web_browser)

    page.btn_enter_in.click()
    time.sleep(1)

    page.btn_registration.click()
    time.sleep(1)

    page.tab_email_register.click()
    time.sleep(1)

    random_email = generate_random_email()

    with allure.step("Тест проверки -- все элементы в панели кликабельны"):
        check.is_true(page.tab_email_register.is_clickable())
        check.is_true(page.tab_phone_register.is_clickable())
        check.is_false(page.btn_register_menu.is_clickable())
        check.is_true(page.btn_enter_register_menu.is_clickable())
        check.is_true(page.btn_eyes_on_password_email.is_clickable())
        check.is_true(page.btn_close.is_visible())

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
        with allure.step("Проверка орфографии"):
            check.equal(element.get_text(), text_element)

    with allure.step("Тест проверки -- ввод в поле 'Имя на кириллице'"):
        page.input_user_name_register_email.send_keys('Артемий')

    with allure.step("Тест проверки -- ввод в поле 'Электронная почта'"):
        page.input_email.send_keys(random_email)

    with allure.step("Тест проверки -- ввод в поле 'Пароль'"):
        page.input_password_register_email.send_keys('SDFDeffgt54')

    page.btn_register_email.click()
    time.sleep(1)

    with allure.step("Тест проверки -- на отображение текста 'Подтверждение почтового адреса'"):
        page.text_passes_email.is_visible()








