import time


import allure
import pytest_check as check
from locators.locators_search_by_parameters import SearchParameters
from conftest import web_browser


@allure.story('Тест поиска автомобилей на "av.by"')
@allure.feature('Тест для проверки поиска автомобилей')
def test_search(web_browser):
    """ Этот тест проверяет кликабельность элементов в поиске автомобилей,
        их наличие на экране"""

    page = SearchParameters(web_browser)

    page.btn_passed_cookie.click()
    time.sleep(1)

    with allure.step("Проверка отображения панели поиска на главной странице"):
        check.is_true(page.panel_search.is_visible(), "Панель поиска не отображается на главной странице")

    with allure.step("Проверка кликабельности элементов в панели поиска"):
        check.is_true(page.btn_brand_car.is_clickable(), "Параметр 'Марка' не кликабельный")
        check.is_true(page.btn_model_car_not.is_clickable(), "Параметр 'Модель' кликабельный")
        check.is_true(page.btn_generation_car_not.is_clickable(), "Параметр 'Поколение' кликабельный")
        check.is_true(page.btn_year.is_clickable(), "Параметр 'Год от' не кликабельный")
        check.is_true(page.btn_to.is_clickable(), "Параметр 'до' не кликабельный")
        check.is_true(page.btn_price_from.is_clickable(), "Параметр 'Цена от' не кликабельный")
        check.is_true(page.btn_price_to.is_clickable(), "Параметр 'до' не кликабельный")
        check.is_true(page.btn_price.is_clickable(), "Параметр 'Валюта' не кликабельный")
        check.is_true(page.btn_volume_from.is_clickable(), "Параметр 'Объём от' не кликабельный")
        check.is_true(page.btn_volume_to.is_clickable(), "Параметр 'до' не кликабельный")
        check.is_true(page.btn_all_parameters.is_clickable(), "Параметр 'Все параметры' не кликабельный")
        check.is_true(page.btn_reset.is_clickable(), "Параметр 'Сбросить' не кликабельный")
        check.is_true(page.btn_show_ad.is_clickable(), "Параметр 'Показать объявление' не кликабельный")

    # Кликаем на 'Модель' в панеле поиска
    page.btn_brand_car.click()
    time.sleep(1)
    page.execute_script('window.scrollBy(0,350);')
    time.sleep(1)

    # Вводим в поиске марку автомобиля
    page.btn_search.send_keys('Porsche')
    time.sleep(1)

    with allure.step("Проверка отображения марки автомобиля после ввода текста"):
        check.is_true(page.brand_car_porsche.is_visible(), "Марка 'Porsche' не отображается после ввода")

    with allure.step("Проверка кликабельности кнопки марки автомобиля"):
        check.is_true(page.brand_car_porsche.is_clickable(), "Кнопка марки 'Porsche' недоступна для клика")

    # Нажатие на кнопку иномарки
    page.brand_car_porsche.click()
    time.sleep(1)

    # Нажатие на кнопку 'Модель'
    page.btn_model_car.click()
    time.sleep(1)

    model_cars = [(page.btn_any, 'Любой'),
                  (page.btn_nine_one_one, '911'),
                  (page.btn_nine_one_four, '914'),
                  (page.btn_nine_two_four, '924'),
                  (page.btn_boxster, 'Boxster'),
                  (page.btn_cayenne, 'Cayenne'),
                  (page.btn_cayenne_coupe, 'Cayenne Coupe'),
                  (page.btn_cayman, 'Cayman'),
                  (page.btn_macan, 'Macan'),
                  (page.btn_panamera, 'Panamera'),
                  (page.btn_taycan, 'Taycan')]

    for locator, text_model in model_cars:
        with allure.step(f"Проверка модели автомобиля: {text_model}"):
            check.is_true(locator.is_visible(), f"Модель '{locator.get_text()}' не отображается")
            check.is_true(locator.is_clickable(), f"Модель '{locator.get_text()}' недоступна для клика")
            check.equal(locator.get_text(), text_model, f"Текст модели '{locator.get_text()}' некорректен")

    # Нажать на модель
    page.btn_nine_one_one.click()
    time.sleep(1)

    # Нажатие на 'Поколение'
    page.btn_generation_car_not.click()
    time.sleep(1)

    with allure.step("Проверка наличие дополнительной панель 'Поколение'"):
        check.is_true(page.panel_all_generations.is_visible(), "Дополнительная панель 'Поколение' не открылась")

    # Выбираем поколение
    page.btn_cars_nine.click()
    time.sleep(1)

    # Кликаем на кнопку 'Показать объявление'
    page.btn_show_ad.click()
    time.sleep(1)

    with allure.step("Проверка перехода по ссылке после нажатия на кнопку 'Показать объявление'"):
        expected_url = "https://cars.av.by/porsche/911/992-2018-"
        check.equal(page.get_current_url(), expected_url, "URL не совпадает")
