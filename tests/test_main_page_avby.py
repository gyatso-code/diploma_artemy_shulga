import time


import allure
import pytest_check as check
from locators.locators_main_avby import MainPageElements
from conftest import web_browser


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки главной страницы -- картинки')
def test_main_img(web_browser):

    page = MainPageElements(web_browser)

    with allure.step("Тест проверки -- на каличество картинок в главной страницы"):
        check.equal(page.img_info.count(), 7)
