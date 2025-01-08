import requests
import allure
import pytest
import json
import pytest_check as check

@allure.story('Тест проверки статус кода на "av.by"')
@allure.feature('Тест для проверки статус кода на странице авторизации')

def test_api_authorization_page():
    """ Этот тест проверяет статус код авторизации на сайте """

    url = "https://api.av.by/auth/phone/sign-in"

    payload = json.dumps({
        "password": "qaartemijtester1110",
        "phone": {
            "country": 1,
            "number": "298593261"
        }
    })
    headers = {
        'accept': '*/*',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://av.by',
        'priority': 'u=1, i',
        'referer': 'https://av.by/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/131.0.0.0 Safari/537.36',
        'x-device-type': 'web.desktop',
        'x-user-group': '386e6d02-3c24-4792-9dcd-9a3aebf8cc84'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)

    with allure.step("Проверка статуса кода на главной странице"):
        check.equal(response.status_code, 200, f'Статус код не равен 200. Статус код равен {response.status_code}')