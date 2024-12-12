import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class RegistrationPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://av.by/'

        super().__init__(web_driver, url)


    # Кнопка войти на главной странице
    btn_enter_in = WebElement(xpath='(//a[@class="nav__link"])[7]')

    # Панель входа
    panel_enter = WebElement(xpath='(//div[@class="drawer__slide-body"])[1]')

    # Ввод поле телефон
    input_phone_and_email = WebElement(xpath='(//input[@class="form-control form-control--large"])[1]')

    # Глазик -- показывающий пароль
    btn_eyes_on_password = WebElement(xpath='(//button[@class="toggle-password-button"])[1]')
    btn_eyes_on_password_email = WebElement(xpath='(//button[@class="toggle-password-button"])[2]')

    # Ввод поле пароль
    input_password = WebElement(xpath='(//input[@name="password"])[1]')

    # Кнопка входа
    btn_enter = WebElement(xpath='//button[@class="button button--action"]')

    # Не помню пароль
    btn_no_remember_password = WebElement(xpath='//button[@class="button button--link button--small"]')

    # Кнопка регистрации
    btn_registration = WebElement(xpath='(//button[@class="drawer__slide-toggle"])[1]')

    # Кнопка входа на странице регистрации
    btn_enter_register_menu = WebElement(xpath='(//button[@class="drawer__slide-toggle"])[1]')

    # Вкладки во входе -- почте или логину
    tab_phone = WebElement(xpath='(//button[@class="tab"])[1]')
    tab_email_and_login = WebElement(xpath='(//button[@class="tab"])[2]')

    # Вкладки в регистрации -- по телефону или почте
    tab_phone_register = WebElement(xpath='(//button[@class="tab"])[1]')
    tab_email_register = WebElement(xpath='(//button[@class="tab"])[2]')

    # Кнопка закрытия
    btn_close = WebElement(xpath='//button[@class="drawer__close"]')

    # Иконка пользователя после входа
    btn_logo_user = WebElement(xpath='//li[@class="nav__item nav__item--user nav__item--dropdown"]')

    # Кнопка регистрации в меню регистрации
    btn_register_menu = WebElement(xpath='(//button[@class="button button--primary"])[1]')
    btn_register_email = WebElement(xpath='(//button[@class="button button--primary"])[2]')

    # Ввод в поле -- Имя на кириллице
    input_user_name_register = WebElement(xpath='(//input[@class="form-control form-control--large"])[1]')
    input_user_name_register_email = WebElement(xpath='(//input[@class="form-control form-control--large"])[4]')

    # Ввод в поле -- Телефон
    input_phone_register = WebElement(xpath='(//input[@class="form-control form-control--large"])[2]')

    # Ввод в поле -- Пароль
    input_password_register = WebElement(xpath='(//input[@class="form-control form-control--large"])[3]')
    input_password_register_email = WebElement(xpath='(//input[@class="form-control form-control--large"])[6]')

    # Текст -- Подтверждение номера телефона
    text_passes_phone = WebElement(xpath='(//div[@class="auth__title"])[3]')
    text_passes_email = WebElement(xpath='(//div[@class="auth__title"])[3]')

    # Ввод в поле -- Электронная почта
    input_email = WebElement(xpath='(//input[@class="form-control form-control--large"])[5]')

    # Текст -- Вход
    text_enter = WebElement(xpath='(//div[@class="auth__title"])[1]')

    # Текст -- Регистрация
    text_registration_menu = WebElement(xpath='(//div[@class="auth__title"])[1]')

    # Текст -- Имя на кириллице
    text_name_on_cyr = WebElement(xpath='(//label[@class="auth__label"])[1]')
    text_name_email_cyr = WebElement(xpath='(//label[@class="auth__label"])[4]')

    # Текст -- Телефон
    text_phone = WebElement(xpath='(//label[@class="auth__label"])[1]')
    text_phone_register = WebElement(xpath='(//label[@class="auth__label"])[2]')

    # Текст -- Пароль
    text_on_password = WebElement(xpath='(//label[@class="auth__label"])[2]')
    text_on_password_register = WebElement(xpath='(//label[@class="auth__label"])[3]')
    text_password_email = WebElement(xpath='//label[@for="regPassword"]')

    # Текст -- Электронная почта
    text_email_register_email = WebElement(xpath='//label[@for="regEmail"]')

    # Текст -- Регистрация и Вход
    text_registration = WebElement(xpath='(//button[@class="drawer__slide-toggle"]//span)[1]')
    text_registration_under = WebElement(xpath='(//button[@class="drawer__slide-toggle"]//small)[1]')
    text_enter_menu_register = WebElement(xpath='(//button[@class="drawer__slide-toggle"]//span)[1]')
    text_enter_menu_register_under = WebElement(xpath='(//button[@class="drawer__slide-toggle"]//small)[1]')

    # Текст -- Электронная почта или логин
    text_email_or_login = WebElement(xpath='(//label[@class="auth__label"])[1]')

    # Текст -- Не короче 8 символов и только латиница и цифры
    text_info_user = WebElement(xpath='(//div[@class="form-hint"])[1]')
    text_info_user_email = WebElement(xpath='(//div[@class="form-hint"])[2]')




