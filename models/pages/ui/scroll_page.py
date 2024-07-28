from selene import browser, have, command


class PageScroll:
    def open(self):
        browser.open('app')

    def check_scroll_offers(self, text):
        browser.element('.recommended-offers box').perform(command.js.scroll_into_view).should(
            have.text(text))

    def check_scroll_id(self, id):
        browser.element('.user-info__id').perform(command.js.scroll_into_view).should(
            have.text(id))
