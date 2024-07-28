import allure
from selene import browser, have, command


class PageScroll:
    def open(self):
        with allure.step("Открыть главную страницу"):
            browser.open('app')

    def check_scroll_offers(self, text):
        with allure.step("Скролл до 'Офферы специально для вас'"):
            browser.element('.recommended-offers box').perform(command.js.scroll_into_view).should(
                have.text(text))

    def check_scroll_id(self, id):
        with allure.step("Скролл до ID пользователя"):
            browser.element('.user-info__id').perform(command.js.scroll_into_view).should(
                have.text(id))


page_scroll = PageScroll()
