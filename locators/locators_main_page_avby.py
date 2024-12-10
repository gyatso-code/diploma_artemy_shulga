import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

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






    # Мобильные приложения
    btn_menu_footer_mobile_app = WebElement(xpath="//div[@class='footer__app-text']//a[@target='_blank']")

    # Приложение для Android
    btn_menu_footer_android = WebElement(xpath='(//a[@class="app-badge"])[1]')

    # Приложение для Android - Текст

    text_menu_footer_android = WebElement(xpath='(//a[@class="app-badge"]//span[@class="app-badge__label"])[1]')
    text_menu_footer_androids = WebElement(xpath='(//a[@class="app-badge"]//span[@class="app-badge__platform"])[1]')

    # Приложение для iPhone
    btn_menu_footer_apple = WebElement(xpath='(//a[@class="app-badge"])[2]')

    # Приложение для Huawei
    btn_menu_footer_huawei = WebElement(xpath='(//a[@class="app-badge"])[3]')

    # Звезды - Рейтинг
    # btn_menu_footer_star_one = WebElement(xpath='(//button[@class="rating__star"])[1]')
    # btn_menu_footer_star_two = WebElement(xpath='(//button[@class="rating__star"])[2]')
    # btn_menu_footer_star_three = WebElement(xpath='(//button[@class="rating__star"])[3]')
    # btn_menu_footer_star_four = WebElement(xpath='(//button[@class="rating__star"])[4]')
    # btn_menu_footer_star_five = WebElement(xpath='(//button[@class="rating__star"])[5]')

    # Задать вопрос
    btn_menu_footer_ask_a_question = WebElement(xpath='(//a[@class="footer__link"])[1]')

    # Правила подачи
    btn_menu_footer_submission_rules = WebElement(xpath='(//a[@class="footer__link"])[2]')

    # Реклама на av.by
    btn_menu_footer_advertising_on = WebElement(xpath='(//a[@class="footer__link"])[3]')

    # Pro-аккаунты
    btn_menu_footer_pro_accounts = WebElement(xpath='(//a[@class="footer__link"])[4]')

    # Спецпроекты
    btn_menu_footer_special_projects = WebElement(xpath='(//a[@class="footer__link"])[5]')

    # Медийная реклама
    btn_menu_footer_display_advertising = WebElement(xpath='(//a[@class="footer__link"])[6]')

    # О проекте
    btn_menu_footer_about_the_project = WebElement(xpath='(//a[@class="footer__link"])[7]')

    # Проверка VIN
    btn_menu_footer_vin_check = WebElement(xpath='(//a[@class="footer__link"])[8]')

    # Оценка стоимости
    btn_menu_footer_cost_estimate = WebElement(xpath='(//a[@class="footer__link"])[9]')

    # Финансы
    btn_menu_footer_finance = WebElement(xpath='(//a[@class="footer__link"])[10]')

    # Услуги
    btn_menu_footer_services = WebElement(xpath='(//a[@class="footer__link"])[11]')

    # Рассрочка
    btn_menu_footer_installment_plan = WebElement(xpath='(//a[@class="footer__link"])[12]')

    # Каталог модификаций
    btn_menu_footer_modification_catalog = WebElement(xpath='(//a[@class="footer__link"])[13]')

    # Таможенный калькулятор
    btn_menu_footer_customs_calculator = WebElement(xpath='(//a[@class="footer__link"])[14]')

    # Печать объявления
    btn_menu_footer_print_advertisement = WebElement(xpath='(//a[@class="footer__link"])[15]')

    # Авто журнал
    btn_menu_footer_auto_magazine = WebElement(xpath='(//a[@class="footer__link"])[16]')

    # Авто с пробегом
    btn_menu_footer_used_car = WebElement(xpath='(//a[@class="footer__link"])[17]')

    # Электромобили
    btn_menu_footer_electric_cars = WebElement(xpath='(//a[@class="footer__link"])[18]')

    # Новые авто
    btn_menu_footer_new_cars = WebElement(xpath='(//a[@class="footer__link"])[19]')

    # Мототехника
    btn_menu_footer_motor_vehicles = WebElement(xpath='(//a[@class="footer__link"])[20]')

    # Сельхозтехника
    btn_menu_footer_agricultural_machinery = WebElement(xpath='(//a[@class="footer__link"])[21]')

    # Грузовики
    btn_menu_footer_trucks = WebElement(xpath='(//a[@class="footer__link"])[22]')

    # Прицепы
    btn_menu_footer_trailers = WebElement(xpath='(//a[@class="footer__link"])[23]')

    # Водный транспорт
    btn_menu_footer_water_transport = WebElement(xpath='(//a[@class="footer__link"])[24]')

    # Спецтехника
    btn_menu_footer_special_equipment = WebElement(xpath='(//a[@class="footer__link"])[25]')

    # Автобусы
    btn_menu_footer_buses = WebElement(xpath='(//a[@class="footer__link"])[26]')

    # Запчасти и авто товары
    btn_menu_footer_spare_and_products = WebElement(xpath='(//a[@class="footer__link"])[27]')

    # Шины и диски
    btn_menu_footer_tires_and_wheels = WebElement(xpath='(//a[@class="footer__link"])[28]')

    # YouTube
    btn_menu_footer_youtube = WebElement(xpath='(//a[@class="footer__link"])[29]')

    # Instagram
    btn_menu_footer_instagram = WebElement(xpath='(//a[@class="footer__link"])[30]')

    # Telegram
    btn_menu_footer_telegram = WebElement(xpath='(//a[@class="footer__link"])[31]')

    # TikTok
    btn_menu_footer_tiktok = WebElement(xpath='(//a[@class="footer__link"])[32]')

    # ВКонтакте
    btn_menu_footer_vk = WebElement(xpath='(//a[@class="footer__link"])[33]')

    # Facebook
    btn_menu_footer_facebook = WebElement(xpath='(//a[@class="footer__link"])[34]')

    # Twitter
    btn_menu_footer_twitter = WebElement(xpath='(//a[@class="footer__link"])[35]')

    # Одноклассники
    btn_menu_footer_classmates = WebElement(xpath='(//a[@class="footer__link"])[36]')

    # Пользовательское соглашение
    btn_menu_footer_users_agreement = WebElement(xpath='//div[@class="footer__links"]//a[1]')

    # Правила обработки персональных данных
    btn_menu_footer_personal_data = WebElement(xpath='//div[@class="footer__links"]//a[2]')

    # Политика использования cookie-файлов
    btn_menu_footer_cookie_files = WebElement(xpath='//div[@class="footer__links"]//button')


