import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPageElements(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://av.by/'

        super().__init__(web_driver, url)

    # Проверить транспорт по VIN, Оценить стоимость авто, Найти услугу в каталоге, Выбрать электомобиль, т.д
    img_info = ManyWebElements(xpath='//a[@class="service-teaser__link"]')
