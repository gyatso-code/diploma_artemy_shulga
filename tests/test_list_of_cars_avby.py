import time

import allure
import pytest_check as check
from locators.locators_list_of_cars import ListCarsMainPageElements
from conftest import web_browser

@allure.story('Тест главной страницы "av.by"')
@allure.feature('Проверка хедера')
def test_list_of_cars(web_browser):
    """Этот тест проверяет кликабельность, наличие элементов, правописание """

    page = ListCarsMainPageElements(web_browser)

    page.btn_all_stamps.click()
    time.sleep(1)


    cars_list = [('Abarth'),('Acura'),('Aito'),('Alfa Romeo'),('Alpina'),('Aston Martin'),('Audi'), 'Avatr'),('BAIC'),
                 'Baojun'),('BAW'),('Belgee'),('Bentley'),('BMW'),('Brilliance'),('Buick'),('BYD'),('Cadillac', 'Changan'),('Chery',
                 'Chevrolet'),('Chrysler'),('Citroen', 'Cupra'),('Dacia'),('Daewoo'),('Daihatsu'),('Datsun'),('Dayun'),('Denza', 'Dodge',
                 'Dongfeng'),('Dongfeng Honda'),('DS'),('EXEED'),('Farizon'),('FAW'),('Ferrari'),('Fiat'),('Ford'),('Foton'),('GAC'),('Geely',
                 'Genesis'),('GMC'),('Great Wall'),('Hafei'),('Haima', 'Haval'),('HiPhi'),('Honda'),('Hongqi'),('Hozon'),('Hummer'),('Hyundai',
                 'Infiniti'),('Iran Khodro'),('Isuzu'),('JAC'),('Jaguar'),('Jeep'),('Jetour'),('Jetta'),('Jiyue'),('Jmev'),('Kaiyi'),('Kia',
                 'Lada (ВАЗ)'),('Lancia'),('Land Rover'),('Leapmotor'),('Lexus'),('Lifan'),('Lincoln'),('Livan'),('LiXiang'),('Lotus'),
                 'Lynk & Co'),('M-Hero'),('Maserati'),('Mazda'),('Mercedes-Benz'),('Mercury'),('MG'),('MINI'),('Mitsubishi',
                 'Nio'),('Nissan'),('Opel'),('Ora'),('Oting'),('Peugeot'),('Plymouth'),('Polar'),('Polestar'),('Pontiac'),('Porsche',
                 'Proton', 'RAM'),('Ravon'),('Renault'),('Renault Samsung'),('Rivian'),('Roewe'),('Rover'),('Saab'),('Saipa'),('Santana',
                 'Saturn'),('Scion'),('SEAT'),('SERES', 'Shenlan'),('Shineray'),('Skoda', 'Skywell'),('Skyworth'),('Smart',
                 'SsangYong'),('Stelato'),('Subaru'),('Suzuki'),('Tata'),('Tesla'),('Think'),('Toyota', 'Trabant'),('Venucia',
                 'VGV'),('Volkswagen'),('Volvo'),('Vortex', 'Voyah'),('Wartburg'),('Weltmeister', 'Wuling'),('Xiaomi', 'Xpeng',
                 'Yudo'),('Zeekr', 'Zotye',
                 'Voyah', 'Wartburg', 'Weltmeister', 'Wuling', 'Xiaomi', 'Xpeng', 'Yudo', 'Zeekr', 'Zotye',
                 'ZX', 'Богдан', 'ГАЗ', 'ЗАЗ', 'ИЖ', 'ЛуАЗ', 'Москвич', 'РАФ', 'ТагАЗ', 'УАЗ', 'Эксклюзив')
    check.greater(page.list_of_cars_element.get_text().find(cars_list), -1)


    # for text in cars_list:
    #     print(page.list_of_cars_element.get_text())
    #     check.equal(page.list_of_cars_element.get_text())


    # with allure.step("Тест проверки -- на кликабельность"):
    #     check.is_true(page.list_of_cars.is_clickable())
    #
    #
    # with allure.step("Тест проверки -- на количество марок машин "):
    #     check.equal(page.list_of_cars.count(), 153)
    #
    #
