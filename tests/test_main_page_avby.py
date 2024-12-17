import time


import allure
import pytest_check as check
from locators.locators_main_avby import MainPageElements
from conftest import web_browser


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки главной страницы -- картинки')
def test_main_img(web_browser):
    """ Этот тест проверяет количество картинок на главной странице """
    page = MainPageElements(web_browser)

    with allure.step("Тест проверки -- количество картинок на главной страницы"):
        check.equal(page.img_info.count(), 7)
