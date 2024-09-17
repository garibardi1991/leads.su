import allure
from selene import browser, have, query
import os
from dotenv import load_dotenv


def load_env():
    load_dotenv()


class AuthenticationForm:

    def open(self):
        with allure.step("Открытие регистрационной формы"):
            browser.open('login')

    def entering_login_password(self):
        with allure.step("Вводим логин и пароль"):
            login = os.getenv('LOG')
            password = os.getenv('PASS')
            browser.element('#webmaster_models_web_LoginForm_email').type(login)
            browser.element('#webmaster_models_web_LoginForm_password').type(password)
            browser.element('[type=submit]').click()

    def check_id(self):
        with allure.step("Проверяем, что вошли под тем пользователем"):
            browser.element('.home').get(query.attribute('.user-info__id'))
            browser.element('.user-info__id').should(have.text('ID 197686'))


authentication_form = AuthenticationForm()
