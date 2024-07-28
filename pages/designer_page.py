from selene import browser, have


class ShowcaseDesigner:
    def open(self):
        browser.open('app/showcase')

    def check_showcase_id(self, id):
        browser.element('.showcase-list__id').should(have.text(id))
