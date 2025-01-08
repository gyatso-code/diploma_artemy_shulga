import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class SearchParameters(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://av.by/'

        super().__init__(web_driver, url)

    # Принятие cookie
    btn_passed_cookie = WebElement(xpath='//button[@class="button button--primary button--block button--large"]')

    # Поиск
    panel_search = WebElement(xpath='//div[@class="filter"]')

    # Марка
    btn_brand_car = WebElement(xpath='(//button[@class="dropdown__control dropdown-floatlabel"])[1]')

    # Модель
    btn_model_car = WebElement(xpath='(//button[@class="dropdown__control dropdown-floatlabel"])[1]')
    btn_model_car_not = WebElement(xpath='(//span[@class="dropdown-floatlabel__box"])[2]')

    # Поколение
    btn_generation_car_not = WebElement(xpath='(//span[@class="dropdown-floatlabel__box"])[3]')

    # Год от
    btn_year = WebElement(xpath='(//button[@class="dropdown__control dropdown-floatlabel"])[3]')

    # До
    btn_to = WebElement(xpath='(//button[@class="dropdown__control dropdown-floatlabel"])[4]')

    # Цена от
    btn_price_from = WebElement(xpath='(//label[@class="richinput-control__box"])[1]')

    # до
    btn_price_to = WebElement(xpath='(//label[@class="richinput-control__box"])[2]')

    # Валюта
    btn_price = WebElement(xpath='(//button[@class="dropdown__control dropdown__control--active dropdown-floatlabel"])[1]')

    # Объём от
    btn_volume_from = WebElement(xpath='(//button[@class="dropdown__control dropdown-floatlabel"])[5]')

    # до
    btn_volume_to = WebElement(xpath='(//button[@class="dropdown__control dropdown-floatlabel"])[6]')

    # Все параметры
    btn_all_parameters = WebElement(xpath='(//button[@class="button button--link"])[1]')

    # Сбросить
    btn_reset = WebElement(xpath='(//button[@class="button button--link"])[2]')

    # Показать объявление
    btn_show_ad = WebElement(xpath='(//div[@class="filter__show-result"])[1]')

    # Поиск
    btn_search = WebElement(xpath='(//input[@class="dropdown__input"])[1]')

    # Марка после ввода текста
    brand_car_porsche = WebElement(xpath='(//button[@class="dropdown__listbutton dropdown__listbutton--focus"])[1]')

    # Любой
    btn_any = WebElement(xpath='(//button[@class="dropdown__listbutton"])[1]')

    # 911
    btn_nine_one_one = WebElement(xpath='(//button[@class="dropdown__listbutton"])[2]')

    # 914
    btn_nine_one_four = WebElement(xpath='(//button[@class="dropdown__listbutton"])[3]')

    # 924
    btn_nine_two_four = WebElement(xpath='(//button[@class="dropdown__listbutton"])[4]')

    # Boxster
    btn_boxster = WebElement(xpath='(//button[@class="dropdown__listbutton"])[5]')

    # Cayenne
    btn_cayenne = WebElement(xpath='(//button[@class="dropdown__listbutton"])[6]')

    # Cayenne Coupe
    btn_cayenne_coupe = WebElement(xpath='(//button[@class="dropdown__listbutton"])[7]')

    # Cayman
    btn_cayman = WebElement(xpath='(//button[@class="dropdown__listbutton"])[8]')

    # Macan
    btn_macan = WebElement(xpath='(//button[@class="dropdown__listbutton"])[9]')

    # Panamera
    btn_panamera = WebElement(xpath='(//button[@class="dropdown__listbutton"])[10]')

    # Taycan
    btn_taycan = WebElement(xpath='(//button[@class="dropdown__listbutton"])[11]')

    # Все поколения
    panel_all_generations = WebElement(xpath='//div[@class="dropdown__cards"]')

    # Карточка 992
    btn_cars_nine = WebElement(xpath='(//div[@class="dropdown__card"])[1]')
