import time

import allure
import pytest_check as check
from locators.locators_footer_avby import FooterPage
from conftest import web_browser


@allure.story('Тест главной страницы "av.by"')
@allure.feature('Проверка футера вкладки')
def test_footers_main(web_browser):
    """Этот тест проверяет кликабельность, наличие элементов, провописание """

    page = FooterPage(web_browser)

    elements = [(page.btn_menu_footer_ask_a_question, 'Задать вопрос', 'https://av.by/support'),
                (page.btn_menu_footer_submission_rules, 'Правила подачи', 'https://av.by/pages/rules'),
                (page.btn_menu_footer_advertising_on, 'Реклама на av.by', 'https://av.by/pages/adv'),
                (page.btn_menu_footer_pro_accounts, 'Pro-аккаунты', 'https://av.by/pages/pro-accounts'),
                (page.btn_menu_footer_special_projects, 'Спецпроекты', 'https://av.by/pages/pr_instruments'),
                (page.btn_menu_footer_display_advertising, 'Медийная реклама', 'https://av.by/pages/index_adv'),
                (page.btn_menu_footer_about_the_project, 'О проекте', 'https://av.by/pages/about'),
                (page.btn_menu_footer_vin_check, 'Проверка VIN', 'https://av.by/vin'),
                (page.btn_menu_footer_cost_estimate, 'Оценка стоимости', 'https://av.by/ocenka-avto'),
                (page.btn_menu_footer_finance, 'Финансы', 'https://av.by/finance'),
                (page.btn_menu_footer_services, 'Услуги', 'https://av.by/company'),
                (page.btn_menu_footer_installment_plan, 'Рассрочка', 'https://av.by/rassrochka'),
                (page.btn_menu_footer_modification_catalog, 'Каталог модификаций', 'https://av.by/catalog'),
                (page.btn_menu_footer_customs_calculator, 'Таможенный калькулятор', 'https://av.by/customs-calculator'),
                (page.btn_menu_footer_print_advertisement, 'Печать объявления', 'https://av.by/print'),
                (page.btn_menu_footer_auto_magazine, 'Автожурнал', 'https://av.by/news'),
                (page.btn_menu_footer_used_car, 'Авто с пробегом', 'https://cars.av.by/'),
                (page.btn_menu_footer_electric_cars, 'Электромобили', 'https://cars.av.by/electrocars'),
                (page.btn_menu_footer_new_cars, 'Новые авто', 'https://salon.av.by/'),
                (page.btn_menu_footer_motor_vehicles, 'Мототехника', 'https://moto.av.by/'),
                (page.btn_menu_footer_agricultural_machinery, 'Сельхозтехника', 'https://agro.av.by/'),
                (page.btn_menu_footer_trucks, 'Грузовики', 'https://truck.av.by/'),
                (page.btn_menu_footer_trailers, 'Прицепы', 'https://trailer.av.by/'),
                (page.btn_menu_footer_water_transport, 'Водный транспорт', 'https://boat.av.by/'),
                (page.btn_menu_footer_special_equipment, 'Спецтехника', 'https://spec.av.by/'),
                (page.btn_menu_footer_buses, 'Автобусы', 'https://bus.av.by/'),
                (page.btn_menu_footer_spare_and_products, 'Запчасти и автотовары', 'https://parts.av.by/'),
                (page.btn_menu_footer_tires_and_wheels, 'Шины и диски', 'https://koleso.av.by/'),
                (page.btn_menu_footer_users_agreement, 'Пользовательское соглашение',
                 'https://av.by/pages/user_agreement'),
                (page.btn_menu_footer_personal_data, 'Правила обработки персональных данных',
                 'https://av.by/privacy_policy'),
                ]

    for element, text_element, url_elements in elements:
        with allure.step("Тест проверки -- правильного URL при переходе"):
            element.click()
            time.sleep(5)
            check.equal(page.get_current_url(), url_elements)

        with allure.step("Проверка на наличие на экране элементов"):
            check.is_true(element.is_visible())

        with allure.step("Проверка орфографии"):
            check.equal(element.get_text(), text_element)

        with allure.step("Тест проверки на правильный адрес кнопки"):
            check.equal(element.get_attribute('href'), url_elements)


@allure.story('Тест главной страницы "av.by"')
@allure.feature('Проверка футера вкладки')
def test_footers_main(web_browser):
    """Этот тест проверяет кликабельность, наличие элементов, провописание """

    page = FooterPage(web_browser)

    elements_app = [
                (page.btn_menu_footer_mobile_app, 'мобильные приложения', 'https://av.by/pages/app'),
                # (page.btn_menu_footer_android, 'Приложение для Android', 'https://play.google.com/store/apps/details?id=by.av.client&utm_source=av_by&utm_medium=footer&utm_campaign=playmarket_icon'),
                # (page.btn_menu_footer_apple, 'Приложение для iPhone', 'https://itunes.apple.com/by/app/av-by-продажа-автомобилей/id1020154366?mt=8'),
                # (page.btn_menu_footer_huawei, 'Приложение для Huawei', 'https://appgallery.huawei.com/'
                #                                                        '#/app/C101652541'),
                (page.btn_menu_footer_youtube, 'YouTube', 'https://www.youtube.com/c/etoavby'),
                (page.btn_menu_footer_instagram, 'Instagram', 'https://www.instagram.com/insta_avby/'),
                (page.btn_menu_footer_telegram, 'Telegram', 'https://t.me/avbynews'),
                (page.btn_menu_footer_tiktok, 'TikTok', 'https://www.tiktok.com/@av.by'),
                # (page.btn_menu_footer_vk, 'ВКонтакте', 'https://vk.com/newsavby'),
                (page.btn_menu_footer_facebook, 'Facebook', 'https://www.facebook.com/belarus.auto'),
                (page.btn_menu_footer_twitter, 'Twitter', 'https://twitter.com/avby_bel'),
                (page.btn_menu_footer_classmates, 'Одноклассники', 'https://ok.ru/av.by')
                ]

    switch_to_window_app = 1
    for element, text_element, url_elements in elements_app:
        with allure.step("Тест проверки правильного URL при переходе"):
            element.click()
            page.switch_to_window(switch_to_window_app)
            time.sleep(3)
            check.equal(page.get_current_url(), url_elements)
            page.switch_to_window(0)
        switch_to_window_app += 1

        with allure.step("Проверка на наличие на экране элементов"):
            check.is_true(element.is_visible())

        with allure.step("Проверка орфографии"):
            check.equal(element.get_text(), text_element)

        with allure.step("Тест проверки на правильный адрес кнопки"):
            check.equal(element.get_attribute('href'), url_elements)
