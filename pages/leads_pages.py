from selene import browser, have
import time
import os
from dotenv import load_dotenv


def load_env():
    load_dotenv()


class AuthenticationForm:

    def open(self):
        browser.open('login')

    def type_log_pass(self):
        login = os.getenv('LOG')
        password = os.getenv('PASS')
        browser.element('#webmaster_models_web_LoginForm_email').type(login)
        browser.element('#webmaster_models_web_LoginForm_password').type(password)
        button = browser.element('[type=submit]')
        button.click()

    def check_id(self):
        time.sleep(5)
        browser.element('.user-info__id').should(have.text('ID 197686'))


class ShowcaseDesigner:
    def open(self):
        browser.open('app/showcase')

    def check_showcase_id(self, id):
        browser.element('.showcase-list__id').should(have.text(id))


class LinkShortener:
    def open(self):
        browser.open('app/linkShortener')

    def input_link(self, text):
        browser.element('#input-url').type(text)

    def button_click(self):
        button = browser.element('.lds-btn.link-shortener-create-form__form-send-btn')
        button.click()

    def checking_link(self, text):
        browser.element('.link-shortener-list-row').should(have.text(text))
