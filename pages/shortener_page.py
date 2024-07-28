from selene import browser, have


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