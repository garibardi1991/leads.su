import json
import requests
from jsonschema import validate
from utils.resource import schema_path


def test_auto_user(base_url):
    response = requests.post(
        base_url + '/Account/v1/Login', data={"userName": "garibardi", "password": "Oly05041987!"}
    )
    body = response.json()
    schema = schema_path('post_method_auto.json')

    assert response.status_code == 200
    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))

def test_no_authorization_user(base_url):
    response = requests.post(
        base_url + '/Account/v1/Login', data={"userName": "garibardi23", "password": "Oly05041987!"}
    )

    assert response.status_code == 200
    assert response.text == ''


def test_books_user(base_url):
    response = requests.get(
        base_url + '/BookStore/v1/Books'
    )
    body = response.json()
    schema = schema_path('get_method_books.json')

    assert response.status_code == 200
    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))

def test_no_delete_user(base_url):
    new_user_id = requests.post(
        base_url + '/Account/v1/User/', data={"userName": "garibardi", "password": "Oly05041987!"}
    ).json()

    response = requests.delete(url=f"{base_url}/Account/v1/User/{new_user_id}")

    assert response.status_code == 401
