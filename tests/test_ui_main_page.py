import time


import allure
import pytest_check as check
from locators.locators_main_page import MainPageElements
from conftest import web_browser


@allure.story('Тест главной страницы "av.by"')
@allure.feature('Тест для проверки элементов на главной страницы')
def test_main_page(web_browser):
    """ Этот тест проверяет кликабельность элементов на главной странице,
     их наличие и корректность переходов по ссылкам"""

    page = MainPageElements(web_browser)

    page.btn_passed_cookie.click()
    time.sleep(1)

    with allure.step("Тест проверки -- на количество картинок в главной страницы"):
        check.equal(page.img_info.count(), 8, "Неверное количество картинок")

    cards_info = [(page.btn_cars_check_vin, 'Проверить транспорт по VIN', 'https://av.by/vin'),
                  (page.btn_cars_add_cars, 'Добавить авто в гараж', 'https://av.by/profile/garage'),
                  (page.btn_price_cars, 'Оценить стоимость авто', 'https://av.by/ocenka-avto'),
                  (page.btn_find_service_cataloge, 'Найти услугу в каталоге', 'https://av.by/company'),
                  (page.btn_choose_electro, 'Выбрать электро­мобиль', 'https://cars.av.by/electrocars'),
                  (page.btn_pick_up_a_loan, 'Подобрать кредит, лизинг, займ', 'https://av.by/finance'),
                  (page.btn_print_ad, 'Печать объявления под стекло', 'https://av.by/print'),
                  (page.btn_play_simulator, 'Поиграть в симулятор перекупа', 'https://av.by/pages/simulator-perekupa'),
                  (page.show_all_announcement, 'Посмотреть все объявления', 'https://cars.av.by/'),
                  (page.show_all_new_car, 'Посмотреть все новые авто', 'https://salon.av.by/'),
                  (page.all_news_avto, 'Все новости в автожурнале', 'https://av.by/news'),
                  (page.btn_sto, 'СТО', 'https://av.by/company/sto'),
                  (page.btn_auto_selection, 'Автоподбор', 'https://av.by/company/autopodbor'),
                  (page.btn_detailing, 'Детейлинг', 'https://av.by/company/detailing'),
                  (page.btn_car_washes, 'Автомойки', 'https://av.by/company/avtomoyki'),
                  (page.btn_driving_school, 'Автошколы', 'https://av.by/company/autoscool'),
                  (page.btn_anti_corrosion_treatment, 'Антикоррозийная обработка',
                   'https://av.by/company/antikarozziynaya-obrabotka'),
                  (page.btn_transport_rental, 'Аренда транспорта', 'https://av.by/company/prokat-avto'),
                  (page.show_all_company, 'Посмотреть все компании', 'https://av.by/company'),
                  (page.car_magazine, 'Автожурнал', 'https://av.by/news'),
                  (page.car_reviews, 'Обзоры автомобилей', 'https://av.by/news/obzory-avtomobilej'),
                  (page.all_car_reviews, 'Все обзоры авто', 'https://av.by/news/obzory-avtomobilej'),
                  (page.news_company, 'Новости компаний', 'https://av.by/news/novosti-kompanij'),
                  (page.all_other_news, 'Все остальные новости', 'https://av.by/news/novosti-kompanij'),
                  (page.all_articles_magazine, 'Все статьи в журнале', 'https://av.by/news'),
                  (page.webpay, 'webpay.by', 'https://webpay.by/')]

    text_main_page = [(page.info_text, 'Обратите внимание, что при оплате банковской платежной картой возврат денежных '
                                       'средств осуществляется на ту же карточку, с которой была произведена оплата. '
                                       'Передача данных осуществляется по отдельному каналу с применением современных '
                                       'методов шифрования. При этом исключается любая возможность перехвата '
                                       'конфиденциальной информации. Данные передаются в зашифрованном виде и '
                                       'сохраняются только на специализированном сервере системы WEBPAY™. После '
                                       'совершения оплаты с использованием банковской карточки необходимо сохранять '
                                       'полученные карт-чеки (подтверждения об оплате, полученные в '
                                       'Интернет⁠-⁠магазине) для сверки с выпиской из карт-счёта '
                                       '(с целью подтверждения совершённых операций в случае возникновения '
                                       'спорных ситуаций). Более подробная информация по оплатам на webpay.by'),
                 (page.info_text_two, 'Расчёты осуществляются в белорусских рублях. Сумма в иностранной валюте '
                                      '(после знака ≈) указана как эквивалент для определения стоимости (цены) '
                                      'в белорусских рублях по курсу НБРБ или определённому рекламодателем '
                                      '(заказчиком).')]

    switch_to_window_main = 1
    for card_info, card_name, card_href in cards_info:
        with allure.step(f"Проверка элемента футера: {card_name}"):
            check.is_true(card_info.is_visible(), "Элемент не виден")
            check.is_true(card_info.is_clickable(), "Кнопка не кликабельна")
            check.equal(card_info.get_attribute('href'), card_href, "Ссылка некорректна")
            check.equal(card_info.get_text(), card_name, "Текст кнопки некорректен")
            card_info.click()
            page.switch_to_window(switch_to_window_main)
            time.sleep(3)
            check.equal(page.get_current_url(), card_href, "URL не совпадает")
            page.switch_to_window(0)
        switch_to_window_main += 1

    for info, text_main in text_main_page:
        check.is_true(info.is_visible(), "Элемент не виден")
        check.equal(info.get_text(), text_main, "Текст некорректен")

