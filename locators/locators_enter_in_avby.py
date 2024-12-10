import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class EnterPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://av.by/'

        super().__init__(web_driver, url)

    # Кнопка войти на главной странице
    btn_enter_in = WebElement(xpath='(//a[@class="nav__link"])[7]')

    # Панель входа
    panel_enter = WebElement(xpath='(//div[@class="drawer__slide-body"])[1]')

    # Ввод поле телефон
    input_phone = WebElement(xpath='(//input[@class="form-control form-control--large"])[1]')

    # Глазик -- показывающий пароль
    eyes_on_password = WebElement(xpath='(//button[@class="toggle-password-button"])[1]')

    # Ввод поле пароль
    input_password = WebElement(xpath='(//input[@name="password"])[1]')

    # Кнопка входа
    btn_enter = WebElement(xpath='//button[@class="button button--action"]')

    # Не помню пароль
    btn_no_remember_password = WebElement(xpath='//button[@class="button button--link button--small"]')

    # Кнопка регистрации
    btn_registration = WebElement(xpath='(//button[@class="drawer__slide-toggle"])[1]')

    # Вкладки  -- почте или логину
    tab_email_and_login = WebElement(xpath='(//button[@class="tab"])[2]')
    tab_phone = WebElement(xpath='(//button[@class="tab"])[1]')


    # Текст -- Вход
    text_enter = WebElement(xpath='(//div[@class="auth__title"])[1]')

    # Текст -- Телефон
    text_phone = WebElement(xpath='(//label[@class="auth__label"])[1]')

    # Текст -- Пароль
    text_on_password = WebElement(xpath='(//label[@class="auth__label"])[2]')

    # Текст -- Регистрация
    text_registration = WebElement(xpath='(//button[@class="drawer__slide-toggle"]//span)[1]')
    text_registration_under = WebElement(xpath='(//button[@class="drawer__slide-toggle"]//small)[1]')



