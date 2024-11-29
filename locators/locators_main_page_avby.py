import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://av.by/'

        super().__init__(web_driver, url)

    # btn_menu_header_logo = WebElement(xpath='//div[@class= "header__logo"]')
    btn_menu_header_announcement = WebElement(xpath='(//a[@class="nav__link"])[1]')
    btn_menu_header_services = WebElement(xpath='(//a[@class="nav__link"])[2]')
    btn_menu_header_magazine = WebElement(xpath='(//a[@class="nav__link"])[3]')
    btn_menu_header_knowledge = WebElement(xpath='(//a[@class="nav__link"])[4]')
    btn_menu_header_attendance = WebElement(xpath='(//a[@class="nav__link"])[5]')
    btn_menu_header_vin_check = WebElement(xpath='(//a[@class="nav__link"])[6]')
    btn_menu_header_login = WebElement(xpath='(//a[@class="nav__link"])[7]')
    # btn_menu_header_login_two = WebElement(xpath='(//div[@class="drawer__slide-body"])[1]')
    # btn_menu_header_place_an_ad = WebElement(xpath='//button[@class="button button--primary button--block button--small"]')




    btn_menu_footer_android = WebElement(xpath='(//a[@class="app-badge"])[1]')
    btn_menu_footer_apple = WebElement(xpath='(//a[@class="app-badge"])[2]')
    btn_menu_footer_huawei = WebElement(xpath='(//a[@class="app-badge"])[3]')
    btn_menu_footer_star_one = WebElement(xpath='(//button[@class="rating__star"])[1]')
    btn_menu_footer_star_two = WebElement(xpath='(//button[@class="rating__star"])[2]')
    btn_menu_footer_star_three = WebElement(xpath='(//button[@class="rating__star"])[3]')
    btn_menu_footer_star_four = WebElement(xpath='(//button[@class="rating__star"])[4]')
    btn_menu_footer_star_five = WebElement(xpath='(//button[@class="rating__star"])[5]')

    btn_menu_footer_ask_a_question = WebElement(xpath='(//a[@class="footer__link"])[1]')
    btn_menu_footer_submission_rules = WebElement(xpath='(//a[@class="footer__link"])[2]')

    btn_menu_footer_advertising_on = WebElement(xpath='(//a[@class="footer__link"])[3]')
    btn_menu_footer_pro_accounts = WebElement(xpath='(//a[@class="footer__link"])[4]')
    btn_menu_footer_special_projects = WebElement(xpath='(//a[@class="footer__link"])[5]')
    btn_menu_footer_display_advertising = WebElement(xpath='(//a[@class="footer__link"])[6]')
    btn_menu_footer_about_the_project = WebElement(xpath='(//a[@class="footer__link"])[7]')





