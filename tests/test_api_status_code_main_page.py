import requests
import allure
import pytest
import pytest_check as check

@allure.story('Тест проверки статус кода на "av.by"')
@allure.feature('Тест для проверки статус кода на главной странице')

def test_api_main_page():
    """ Этот тест проверяет статус код главной страницы сайта """

    url = "https://av.by/"

    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': '_ym_uid=1733511427899934975; _ym_d=1733511427; _ga=GA1.1.1236547443.1733511429; '
                  'userGroup=386e6d02-3c24-4792-9dcd-9a3aebf8cc84; acceptedCookies={%22accepted%22:'
                  'true%2C%22analytical%22:true%2C%22technical%22:true%2C%22promotion%22:true}; DEVICE_TYPE=desktop; '
                  'DEBUG_CURRENT_DEVICE_TYPE=desktop; _ym_isad=2; __gads=ID=505849818f643572:T=1733511922:RT=1736202814'
                  ':S=ALNI_MY5PD3ybrhUioxwf3B9Hu78C9jtsg; __gpi=UID=00000f65dfd00b1a:T=1733511922:RT=1736202814:'
                  'S=ALNI_Ma_VwiYf16m6GQ-3BJdIM92MNYSwA; __eoi=ID=60b0496b4994204e:T=1733511922:RT=1736202814:'
                  'S=AA-AfjZf1Izs2WNzi8CwRCgXd-b6; _ga_GWM6BXJZNK=GS1.1.1736202877.25.1.1736202900.37.0.0; '
                  'DEBUG_CURRENT_DEVICE_TYPE=desktop; DEVICE_TYPE=desktop',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/131.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)

    with allure.step("Проверка статуса кода на главной странице"):
        check.equal(response.status_code, 200, f'Статус код не равен 200. Статус код равен {response.status_code}')

