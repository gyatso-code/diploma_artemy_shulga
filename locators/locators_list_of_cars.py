import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class ListCarsMainPageElements(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://av.by/'

        super().__init__(web_driver, url)

    # Кнопка -- Все марки
    btn_all_stamps = WebElement(xpath='//button[@class="button button--default button--small"]')

    # Лист всех марок
    list_of_cars = ManyWebElements(xpath='//li[@class="catalog__item"]//span[@class="catalog__title"]')

    list_of_cars_element = WebElement(xpath='//div[@class="catalog__list"]')