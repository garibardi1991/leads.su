from selene import browser, have
import time


class AuthenticationForm:
    def open(self):
        browser.open('login')

    def type_log_pass(self):
        browser.element('#webmaster_models_web_LoginForm_email').type('test@leads.su')
        browser.element('#webmaster_models_web_LoginForm_password').type('123456')
        button = browser.element('[type=submit]')
        button.click()

    def check_id(self):
        time.sleep(5)
        browser.element('.user-info__id').should(have.text('ID 13714'))
