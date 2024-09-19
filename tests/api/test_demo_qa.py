import json
import requests
from allure_commons.types import Severity
from jsonschema import validate

from utils.requests_helper import api_request

from utils.resource import schema_path
import allure


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Авторизация на DemoQA")
@allure.story("Тестирование запроса на авторизацию")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_auto_user(base_url):
    response = api_request(method="POST", base_api_url=base_url, endpoint='/Account/v1/Login',
                           data={"userName": "garibardi", "password": "Oly05041987!"}
                           )
    body = response.json()
    schema = schema_path('post_method_auto.json')
    with allure.step('Проверяем что статус кода == 200'):
        assert response.status_code == 200
    with allure.step('Проверка JSON schema'):
        with open(schema) as file:
            f = file.read()
            validate(body, schema=json.loads(f))


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Некорректная авторизация на DemoQA")
@allure.story("Тестирование запроса на некорректную авторизацию")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_no_authorization_user(base_url):
    response = api_request(method="POST", base_api_url=base_url, endpoint='/Account/v1/Login',
                           data={"userName": "garibardi123", "password": "Oly05041987!"}
                           )
    with allure.step('Проверяем что статус кода == 200'):
        assert response.status_code == 200
    with allure.step('Проверяем, что вернулся пустой текст, подтверждающий некорректную авторизацию'):
        try:
            json_response = response.json()
            assert json_response is None or json_response == {}
        except ValueError:
            assert response.text.strip() == ''


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Проверка вывода книг пользователя на DemoQA")
@allure.story("Тестирование запроса на вывод книг пользователя")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_books_user(base_url):
    response = api_request(method="GET",
        base_api_url=base_url, endpoint='/BookStore/v1/Books'
    )
    body = response.json()
    schema = schema_path('get_method_books.json')
    with allure.step('Проверяем что статус кода == 200'):
        assert response.status_code == 200
    with allure.step('Проверка JSON schema'):
        with open(schema) as file:
            f = file.read()
            validate(body, schema=json.loads(f))


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Некорректный запрос на удаление аккаунта")
@allure.story("Тестирование запроса на удаление аккаунта")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_no_delete_user(base_url):
    new_user_id = api_request(method="POST",
        base_api_url=base_url, endpoint='/Account/v1/User/', data={"userName": "garibardi", "password": "Oly05041987!"}
    ).json()

    response = requests.delete(url=f"{base_url}/Account/v1/User/{new_user_id}")
    with allure.step('Проверяем что статус кода == 401'):
        assert response.status_code == 401
