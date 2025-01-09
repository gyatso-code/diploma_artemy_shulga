import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPageElements(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://av.by/'

        super().__init__(web_driver, url)


    # Принятие cookie

    btn_passed_cookie = WebElement(xpath='//button[@class="button button--primary button--block button--large"]')

    # Логотип av.by YouTube
    btn_logo_youtube = WebElement(xpath='//a[@class="general-brand__link"]')

    # Карточка -- Проверить транспорт по Vin
    btn_cars_check_vin = WebElement(xpath='(//a[@class="service-teaser__link"])[1]')

    # Карточка -- Добавить авто в гараж
    btn_cars_add_cars = WebElement(xpath='(//a[@class="service-teaser__link"])[2]')

    # Карточка -- Оценить стоимость авто
    btn_price_cars = WebElement(xpath='(//a[@class="service-teaser__link"])[3]')

    # Карточка -- Найди услугу в каталоге
    btn_find_service_cataloge = WebElement(xpath='(//a[@class="service-teaser__link"])[4]')

    # Карточка -- Выбрать электромобиль
    btn_choose_electro = WebElement(xpath='(//a[@class="service-teaser__link"])[5]')

    # Карточка -- Подобрать кредит, лизинг, займ
    btn_pick_up_a_loan = WebElement(xpath='(//a[@class="service-teaser__link"])[6]')

    # Карточка -- Печать объявления под стекло
    btn_print_ad = WebElement(xpath='(//a[@class="service-teaser__link"])[7]')

    # Каточка -- Поиграть в симулятор перекупа
    btn_play_simulator = WebElement(xpath='(//a[@class="service-teaser__link"])[8]')

    # Все картинки
    img_info = ManyWebElements(xpath='//a[@class="service-teaser__link"]')


    # # Как сюда попасть
    # how_here_getin = WebElement(xpath='(//a[@target="_blank"])[10]')

    # Посмотреть все объявление
    show_all_announcement = WebElement(xpath='(//a[@class="button button--common button--block button--x-large"])[1]')

    # Посмотреть все новые авто
    show_all_new_car = WebElement(xpath='(//a[@class="button button--common button--block button--x-large"])[2]')

    # Все новости в автожурнале
    all_news_avto = WebElement(xpath='(//a[@class="button button--common button--block button--x-large"])[3]')

    # Посмотреть все компании
    show_all_company = WebElement(xpath='(//a[@class="button button--common button--block button--x-large"])[4]')

    # Автожурнал
    car_magazine = WebElement(xpath='(//a[@class="journal-logo__link"])[1]')

    # Youtube av.by
    youtube_av_by = WebElement(xpath='(//a[@class="journal-youtube__link"])[1]')

    # Обзоры автомобилей
    car_reviews = WebElement(xpath='(//a[@class="journal-inline__link"])[1]')

    # Все обзоры авто
    all_car_reviews = WebElement(xpath='(//a[@class="button button--common button--block button--x-large"])[5]')

    # Новости компаний
    news_company = WebElement(xpath='(//a[@class="journal-inline__link"])[2]')

    # Все остальные новости
    all_other_news = WebElement(xpath='(//a[@class="button button--common button--block button--x-large"])[6]')

    # Все статьи в журнале
    all_articles_magazine = WebElement(xpath='(//a[@class="button button--common button--block button--x-large"])[7]')

    # СТО
    btn_sto = WebElement(xpath='(//a[@class="companies-category__link"])[1]')

    # Автоподбор
    btn_auto_selection = WebElement(xpath='(//a[@class="companies-category__link"])[2]')

    # Детейлинг
    btn_detailing = WebElement(xpath='(//a[@class="companies-category__link"])[3]')

    # Автомойки
    btn_car_washes = WebElement(xpath='(//a[@class="companies-category__link"])[4]')

    # Автошколы
    btn_driving_school = WebElement(xpath='(//a[@class="companies-category__link"])[5]')

    # Антикоррозийная обработка
    btn_anti_corrosion_treatment = WebElement(xpath='(//a[@class="companies-category__link"])[6]')

    # Аренда транспорта
    btn_transport_rental = WebElement(xpath='(//a[@class="companies-category__link"])[7]')

    # Инфо текст
    info_text = WebElement(xpath='(//p[@class="payment-info__description"])[1]')

    # Инфо текст второй
    info_text_two = WebElement(xpath='(//p[@class="payment-info__description"])[2]')

    # webpay.by
    webpay = WebElement(xpath='(//a[@rel="nofollow noopener noreferrer"])[1]')