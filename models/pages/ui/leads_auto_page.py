from selene import browser, have
import time
import os
from dotenv import load_dotenv


def load_env():
    load_dotenv()


class AuthenticationForm:

    def open(self):
        browser.open('login')

    def entering_login_password(self):
        login = os.getenv('LOG')
        password = os.getenv('PASS')
        browser.element('#webmaster_models_web_LoginForm_email').type(login)
        browser.element('#webmaster_models_web_LoginForm_password').type(password)
        browser.element('[type=submit]').click()

    def check_id(self):
        time.sleep(5)
        browser.element('.user-info__id').should(have.text('ID 197686'))
