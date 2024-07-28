import allure
from selene import browser, have


class LinkShortener:
    def open(self):
        with allure.step("Открытие сокращатора ссылок"):
            browser.open('app/linkShortener')

    def input_link(self, text):
        with allure.step("Ввод сокращаемой ссылки"):
            browser.element('#input-url').type(text)

    def button_click(self):
        with allure.step("Нажатие кнопки сократить"):
            button = browser.element('.lds-btn.link-shortener-create-form__form-send-btn')
            button.click()

    def checking_link(self, text):
        with allure.step("Проверка что сократили данную ссылку"):
            browser.element('.link-shortener-list-row').should(have.text(text))


link_shortener = LinkShortener()
