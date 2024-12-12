import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class HeaderPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://av.by/'

        super().__init__(web_driver, url)

    # Объявления
    btn_menu_header_announcement = WebElement(xpath='(//a[@class="nav__link"])[1]')

    # Сервисы
    btn_menu_header_services = WebElement(xpath='(//a[@class="nav__link"])[2]')

    # Журнал
    btn_menu_header_magazine = WebElement(xpath='(//a[@class="nav__link"])[3]')

    # Знания
    btn_menu_header_knowledge = WebElement(xpath='(//a[@class="nav__link"])[4]')

    # Услуги
    btn_menu_header_attendance = WebElement(xpath='(//a[@class="nav__link"])[5]')

    # Проверка VIN
    btn_menu_header_vin_check = WebElement(xpath='(//a[@class="nav__link"])[6]')

    # Войти
    btn_menu_header_login = WebElement(xpath='(//a[@class="nav__link"])[7]')

    # Подать объявление
    btn_menu_header_place_an_ad = WebElement(xpath='//button[@class="button button'
                                                   '--primary button--block button--small"]')

