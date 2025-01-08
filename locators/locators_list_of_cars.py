import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class ListCarsMainPageElements(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://av.by/'

        super().__init__(web_driver, url)

    # Кнопка -- Все марки
    btn_all_stamps = WebElement(xpath='//button[@class="button button--default button--small"]')


    # Машина Abarth
    btn_list_cars_abarth = WebElement(xpath='(//a[@class="catalog__link"])[1]')

    # Машина Acura
    btn_list_cars_acura = WebElement(xpath='(//a[@class="catalog__link"])[2]')

    # Машина Aito
    btn_list_cars_aito = WebElement(xpath='(//a[@class="catalog__link"])[3]')

    # Машина Alfa Romeo
    btn_list_cars_alfa_romeo = WebElement(xpath='(//a[@class="catalog__link"])[4]')

    # Машина Alpina
    btn_list_cars_alpina = WebElement(xpath='(//a[@class="catalog__link"])[5]')

    # Машина Audi
    btn_list_cars_audi = WebElement(xpath='(//a[@class="catalog__link"])[6]')

    # Машина Avatr
    btn_list_cars_avatr = WebElement(xpath='(//a[@class="catalog__link"])[7]')

    # Машина BAIC
    btn_list_cars_baic = WebElement(xpath='(//a[@class="catalog__link"])[8]')

    # Машина Baojun
    btn_list_cars_baojun = WebElement(xpath='(//a[@class="catalog__link"])[9]')

    # Машина BAW
    btn_list_cars_baw = WebElement(xpath='(//a[@class="catalog__link"])[10]')

    # Машина Belgee
    btn_list_cars_belgee = WebElement(xpath='(//a[@class="catalog__link"])[11]')

    # Машина Bentley
    btn_list_cars_bentley = WebElement(xpath='(//a[@class="catalog__link"])[12]')

    # Машина BMW
    btn_list_cars_bmw = WebElement(xpath='(//a[@class="catalog__link"])[13]')

    # Машина Brilliance
    btn_list_cars_brilliance = WebElement(xpath='(//a[@class="catalog__link"])[14]')

    # Машина Buick
    btn_list_cars_buick = WebElement(xpath='(//a[@class="catalog__link"])[15]')

    # Машина BYD
    btn_list_cars_byd = WebElement(xpath='(//a[@class="catalog__link"])[16]')

    # Машина Cadillac
    btn_list_cars_cadillac = WebElement(xpath='(//a[@class="catalog__link"])[17]')

    # Машина Changan
    btn_list_cars_changan = WebElement(xpath='(//a[@class="catalog__link"])[18]')

    # Машина Chery
    btn_list_cars_chery = WebElement(xpath='(//a[@class="catalog__link"])[19]')

    # Машина Chevrolet
    btn_list_cars_chevrolet = WebElement(xpath='(//a[@class="catalog__link"])[20]')

    # Машина Chrysler
    btn_list_cars_chrysler = WebElement(xpath='(//a[@class="catalog__link"])[21]')

    # Машина Citroen
    btn_list_cars_citroen = WebElement(xpath='(//a[@class="catalog__link"])[22]')

    # Машина Cupra
    btn_list_cars_cupra = WebElement(xpath='(//a[@class="catalog__link"])[23]')

    # Машина Dacia
    btn_list_cars_dacia = WebElement(xpath='(//a[@class="catalog__link"])[24]')

    # Машина Daewoo
    btn_list_cars_daewoo = WebElement(xpath='(//a[@class="catalog__link"])[25]')

    # Машина Daihatsu
    btn_list_cars_daihatsu = WebElement(xpath='(//a[@class="catalog__link"])[26]')

    # Машина Datsun
    btn_list_cars_datsun = WebElement(xpath='(//a[@class="catalog__link"])[27]')

    # Машина Dayun
    btn_list_cars_dayun = WebElement(xpath='(//a[@class="catalog__link"])[28]')

    # Машина Denza
    btn_list_cars_denza = WebElement(xpath='(//a[@class="catalog__link"])[29]')

    # Машина Dodge
    btn_list_cars_dodge = WebElement(xpath='(//a[@class="catalog__link"])[30]')

    # Машина Dongfeng
    btn_list_cars_dongfeng = WebElement(xpath='(//a[@class="catalog__link"])[31]')

    # Машина Dongfeng Honda
    btn_list_cars_dongfeng_honda = WebElement(xpath='(//a[@class="catalog__link"])[32]')

    # Машина DS
    btn_list_cars_dc = WebElement(xpath='(//a[@class="catalog__link"])[33]')

    # Машина EXEED
    btn_list_cars_exeed = WebElement(xpath='(//a[@class="catalog__link"])[34]')

    # Машина Farizon
    btn_list_cars_farizon = WebElement(xpath='(//a[@class="catalog__link"])[35]')

    # Машина FAW
    btn_list_cars_faw = WebElement(xpath='(//a[@class="catalog__link"])[36]')

    # Машина Ferrari
    btn_list_cars_ferrari = WebElement(xpath='(//a[@class="catalog__link"])[37]')

    # Машина Fiat
    btn_list_cars_fiat = WebElement(xpath='(//a[@class="catalog__link"])[38]')

    # Машина Ford
    btn_list_cars_ford = WebElement(xpath='(//a[@class="catalog__link"])[39]')

    # Машина Foton
    btn_list_cars_foton = WebElement(xpath='(//a[@class="catalog__link"])[40]')

    # Машина GAC
    btn_list_cars_gac = WebElement(xpath='(//a[@class="catalog__link"])[41]')

    # Машина Geely
    btn_list_cars_geely = WebElement(xpath='(//a[@class="catalog__link"])[42]')

    # Машина Genesis
    btn_list_cars_genesis = WebElement(xpath='(//a[@class="catalog__link"])[43]')

    # Машина GMC
    btn_list_cars_gmc = WebElement(xpath='(//a[@class="catalog__link"])[44]')

    # Машина Great Wall
    btn_list_cars_great_wall = WebElement(xpath='(//a[@class="catalog__link"])[45]')

    # Машина Hafei
    btn_list_cars_hafei = WebElement(xpath='(//a[@class="catalog__link"])[46]')

    # Машина Haima
    btn_list_cars_haima = WebElement(xpath='(//a[@class="catalog__link"])[47]')

    # Машина Haval
    btn_list_cars_haval = WebElement(xpath='(//a[@class="catalog__link"])[48]')

    # Машина HiPhi
    btn_list_cars_hiphi = WebElement(xpath='(//a[@class="catalog__link"])[49]')

    # Машина Honda
    btn_list_cars_honda = WebElement(xpath='(//a[@class="catalog__link"])[50]')

    # Машина Hongqi
    btn_list_cars_hongqi = WebElement(xpath='(//a[@class="catalog__link"])[51]')

    # Машина Hozon
    btn_list_cars_hozon = WebElement(xpath='(//a[@class="catalog__link"])[52]')

    # Машина Hummer
    btn_list_cars_hummer = WebElement(xpath='(//a[@class="catalog__link"])[53]')

    # Машина Hyundai
    btn_list_cars_hyundai = WebElement(xpath='(//a[@class="catalog__link"])[54]')

    # Машина Infiniti
    btn_list_cars_infiniti = WebElement(xpath='(//a[@class="catalog__link"])[55]')

    # Машина Iran Khodro
    btn_list_cars_khodro = WebElement(xpath='(//a[@class="catalog__link"])[56]')

    # Машина Isuzu
    btn_list_cars_isuzu = WebElement(xpath='(//a[@class="catalog__link"])[57]')

    # Машина JAC
    btn_list_cars_jac = WebElement(xpath='(//a[@class="catalog__link"])[58]')

    # Машина Jaguar
    btn_list_cars_jaguar = WebElement(xpath='(//a[@class="catalog__link"])[59]')

    # Машина Jeep
    btn_list_cars_jeep = WebElement(xpath='(//a[@class="catalog__link"])[60]')

    # Машина Jetour
    btn_list_cars_jetour = WebElement(xpath='(//a[@class="catalog__link"])[61]')

    # Машина Jetta
    btn_list_cars_jetta = WebElement(xpath='(//a[@class="catalog__link"])[62]')

    # Машина Jiyue
    btn_list_cars_jiyue = WebElement(xpath='(//a[@class="catalog__link"])[63]')

    # Машина Jmev
    btn_list_cars_jmev = WebElement(xpath='(//a[@class="catalog__link"])[64]')

    # Машина Kaiyi
    btn_list_cars_kaiyi = WebElement(xpath='(//a[@class="catalog__link"])[65]')

    # Машина Kia
    btn_list_cars_kia = WebElement(xpath='(//a[@class="catalog__link"])[66]')

    # Машина Lada (ВАЗ)
    btn_list_cars_lada = WebElement(xpath='(//a[@class="catalog__link"])[67]')

    # Машина Lancia
    btn_list_cars_lancia = WebElement(xpath='(//a[@class="catalog__link"])[68]')

    # Машина Land Rover
    btn_list_cars_rover = WebElement(xpath='(//a[@class="catalog__link"])[69]')

    # Машина Leapmotor
    btn_list_cars_leapmotor = WebElement(xpath='(//a[@class="catalog__link"])[70]')

    # Машина Lexus
    btn_list_cars_lexus = WebElement(xpath='(//a[@class="catalog__link"])[71]')

    # Машина Lifan
    btn_list_cars_lifan = WebElement(xpath='(//a[@class="catalog__link"])[72]')

    # Машина Lincoln
    btn_list_cars_lincoln = WebElement(xpath='(//a[@class="catalog__link"])[73]')

    # Машина Livan
    btn_list_cars_livan = WebElement(xpath='(//a[@class="catalog__link"])[74]')

    # Машина LiXiang
    btn_list_cars_lixiang = WebElement(xpath='(//a[@class="catalog__link"])[75]')

    # Машина Lotus
    btn_list_cars_lotus = WebElement(xpath='(//a[@class="catalog__link"])[76]')

    # Машина Lynk & Co
    btn_list_cars_lynk = WebElement(xpath='(//a[@class="catalog__link"])[77]')

    # Машина M-Hero
    btn_list_cars_hero = WebElement(xpath='(//a[@class="catalog__link"])[78]')

    # Машина Maserati
    btn_list_cars_maserati = WebElement(xpath='(//a[@class="catalog__link"])[79]')

    # Машина Mazda
    btn_list_cars_mazda = WebElement(xpath='(//a[@class="catalog__link"])[80]')

    # Машина Mercedes-Benz
    btn_list_cars_benz = WebElement(xpath='(//a[@class="catalog__link"])[81]')

    # Машина Mercury
    btn_list_cars_mercury = WebElement(xpath='(//a[@class="catalog__link"])[82]')

    # Машина MG
    btn_list_cars_mg = WebElement(xpath='(//a[@class="catalog__link"])[83]')

    # Машина MINI
    btn_list_cars_mini = WebElement(xpath='(//a[@class="catalog__link"])[84]')

    # Машина Mitsubishi
    btn_list_cars_mitsubishi = WebElement(xpath='(//a[@class="catalog__link"])[85]')

    # Машина Nio
    btn_list_cars_nio = WebElement(xpath='(//a[@class="catalog__link"])[86]')

    # Машина Nissan
    btn_list_cars_nissan = WebElement(xpath='(//a[@class="catalog__link"])[87]')

    # Машина Opel
    btn_list_cars_opel = WebElement(xpath='(//a[@class="catalog__link"])[88]')

    # Машина Ora
    btn_list_cars_ora = WebElement(xpath='(//a[@class="catalog__link"])[89]')

    # Машина Oting
    btn_list_cars_oting = WebElement(xpath='(//a[@class="catalog__link"])[90]')

    # Машина Peugeot
    btn_list_cars_peugeot = WebElement(xpath='(//a[@class="catalog__link"])[91]')

    # Машина Plymouth
    btn_list_cars_plymouth = WebElement(xpath='(//a[@class="catalog__link"])[92]')

    # Машина Polar
    btn_list_cars_polar = WebElement(xpath='(//a[@class="catalog__link"])[93]')

    # Машина Polestar
    btn_list_cars_polestar = WebElement(xpath='(//a[@class="catalog__link"])[94]')

    # Машина Pontiac
    btn_list_cars_pontiac = WebElement(xpath='(//a[@class="catalog__link"])[95]')

    # Машина Porsche
    btn_list_cars_porsche = WebElement(xpath='(//a[@class="catalog__link"])[96]')

    # Машина Proton
    btn_list_cars_proton = WebElement(xpath='(//a[@class="catalog__link"])[97]')

    # Машина RAM
    btn_list_cars_ram = WebElement(xpath='(//a[@class="catalog__link"])[98]')

    # Машина Ravon
    btn_list_cars_ravon = WebElement(xpath='(//a[@class="catalog__link"])[99]')

    # Машина Renault
    btn_list_cars_renault = WebElement(xpath='(//a[@class="catalog__link"])[100]')

    # Машина Renault Samsung
    btn_list_cars_samsung = WebElement(xpath='(//a[@class="catalog__link"])[101]')

    # Машина Rivian
    btn_list_cars_rivian = WebElement(xpath='(//a[@class="catalog__link"])[102]')

    # Машина Roewe
    btn_list_cars_roewe = WebElement(xpath='(//a[@class="catalog__link"])[103]')

    # Машина Rolls-Royce
    btn_list_cars_royce = WebElement(xpath='(//a[@class="catalog__link"])[104]')

    # Машина Rover
    btn_list_cars_rovers = WebElement(xpath='(//a[@class="catalog__link"])[105]')

    # Машина Saab
    btn_list_cars_saab = WebElement(xpath='(//a[@class="catalog__link"])[106]')

    # Машина Saipa
    btn_list_cars_saipa = WebElement(xpath='(//a[@class="catalog__link"])[107]')

    # Машина Santana
    btn_list_cars_santana = WebElement(xpath='(//a[@class="catalog__link"])[108]')

    # Машина Saturn
    btn_list_cars_saturn = WebElement(xpath='(//a[@class="catalog__link"])[109]')

    # Машина Scion
    btn_list_cars_scion = WebElement(xpath='(//a[@class="catalog__link"])[110]')

    # Машина SEAT
    btn_list_cars_seat = WebElement(xpath='(//a[@class="catalog__link"])[111]')

    # Машина SERES
    btn_list_cars_seres = WebElement(xpath='(//a[@class="catalog__link"])[112]')

    # Машина Shenlan
    btn_list_cars_shenlan = WebElement(xpath='(//a[@class="catalog__link"])[113]')

    # Машина Shineray
    btn_list_cars_shineray = WebElement(xpath='(//a[@class="catalog__link"])[114]')

    # Машина Skoda
    btn_list_cars_scoda = WebElement(xpath='(//a[@class="catalog__link"])[115]')

    # Машина Skywell
    btn_list_cars_skywell = WebElement(xpath='(//a[@class="catalog__link"])[116]')

    # Машина Skyworth
    btn_list_cars_skyworth = WebElement(xpath='(//a[@class="catalog__link"])[117]')

    # Машина Smart
    btn_list_cars_smart = WebElement(xpath='(//a[@class="catalog__link"])[118]')

    # Машина SsangYong
    btn_list_cars_youn = WebElement(xpath='(//a[@class="catalog__link"])[119]')

    # Машина Stelato
    btn_list_cars_stelato = WebElement(xpath='(//a[@class="catalog__link"])[120]')

    # Машина Subaru
    btn_list_cars_subaru = WebElement(xpath='(//a[@class="catalog__link"])[121]')

    # Машина Suzuki
    btn_list_cars_suzuki = WebElement(xpath='(//a[@class="catalog__link"])[122]')

    # Машина Tank
    btn_list_cars_tank = WebElement(xpath='(//a[@class="catalog__link"])[123]')

    # Машина Tata
    btn_list_cars_tata = WebElement(xpath='(//a[@class="catalog__link"])[124]')

    # Машина Tesla
    btn_list_cars_tesla = WebElement(xpath='(//a[@class="catalog__link"])[125]')

    # Машина Think
    btn_list_cars_think = WebElement(xpath='(//a[@class="catalog__link"])[126]')

    # Машина Toyota
    btn_list_cars_toyota = WebElement(xpath='(//a[@class="catalog__link"])[127]')

    # Машина Trabant
    btn_list_cars_trabant = WebElement(xpath='(//a[@class="catalog__link"])[128]')

    # Машина Venucia
    btn_list_cars_venucia = WebElement(xpath='(//a[@class="catalog__link"])[129]')

    # Машина VGV
    btn_list_cars_vgv = WebElement(xpath='(//a[@class="catalog__link"])[130]')

    # Машина Volkswagen
    btn_list_cars_volkswagen = WebElement(xpath='(//a[@class="catalog__link"])[131]')

    # Машина Volvo
    btn_list_cars_volvo = WebElement(xpath='(//a[@class="catalog__link"])[132]')

    # Машина Vortex
    btn_list_cars_vortex = WebElement(xpath='(//a[@class="catalog__link"])[133]')

    # Машина Voyah
    btn_list_cars_voyah = WebElement(xpath='(//a[@class="catalog__link"])[134]')

    # Машина Wartburg
    btn_list_cars_wartburg = WebElement(xpath='(//a[@class="catalog__link"])[135]')

    # Машина Weltmeister
    btn_list_cars_weltmeister = WebElement(xpath='(//a[@class="catalog__link"])[136]')

    # Машина Wuling
    btn_list_cars_wuling = WebElement(xpath='(//a[@class="catalog__link"])[137]')

    # Машина Xiaomi
    btn_list_cars_xiaomi = WebElement(xpath='(//a[@class="catalog__link"])[138]')

    # Машина Xpeng
    btn_list_cars_xpeng = WebElement(xpath='(//a[@class="catalog__link"])[139]')

    # Машина Zeekr
    btn_list_cars_zeekr = WebElement(xpath='(//a[@class="catalog__link"])[140]')

    # Машина Zotye
    btn_list_cars_zotye = WebElement(xpath='(//a[@class="catalog__link"])[141]')

    # Машина ZX
    btn_list_cars_zx = WebElement(xpath='(//a[@class="catalog__link"])[142]')

    # Машина Богдан
    btn_list_cars_bogdan = WebElement(xpath='(//a[@class="catalog__link"])[143]')

    # Машина ГАЗ
    btn_list_cars_gaz = WebElement(xpath='(//a[@class="catalog__link"])[144]')

    # Машина ЗАЗ
    btn_list_cars_zaz = WebElement(xpath='(//a[@class="catalog__link"])[145]')

    # Машина ИЖ
    btn_list_cars_izh = WebElement(xpath='(//a[@class="catalog__link"])[146]')

    # Машина ЛуАЗ
    btn_list_cars_lyaz = WebElement(xpath='(//a[@class="catalog__link"])[147]')

    # Машина Москвич
    btn_list_cars_moskich = WebElement(xpath='(//a[@class="catalog__link"])[148]')

    # Машина РАФ
    btn_list_cars_raf = WebElement(xpath='(//a[@class="catalog__link"])[149]')

    # Машина ТагАЗ
    btn_list_cars_tagaz = WebElement(xpath='(//a[@class="catalog__link"])[150]')

    # Машина УАЗ
    btn_list_cars_yaz = WebElement(xpath='(//a[@class="catalog__link"])[151]')

    # Машина Эксклюзив
    btn_list_cars_exclusive = WebElement(xpath='(//a[@class="catalog__link"])[152]')


    # Лист всех марок
    list_of_cars = ManyWebElements(xpath='//li[@class="catalog__item"]//span[@class="catalog__title"]')
