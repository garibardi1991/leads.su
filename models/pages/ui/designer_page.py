import allure
from selene import browser, have


class ShowcaseDesigner:
    def open(self):
        with allure.step("Открытие конструктора витрин"):
            browser.open('app/showcase')

    def check_showcase_id(self, id):
        with allure.step("Проверка нахождения витрины по ID в списке"):
            browser.element('.showcase-list__id').should(have.text(id))


showcase_designer = ShowcaseDesigner()
