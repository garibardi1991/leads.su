import allure
from allure_commons.types import Severity
from models.pages.ui.shortener_page import link_shortener


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Сокращатор ссылок")
@allure.story("Тестирование сокращатора ссылок")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_link_shortener():
    link_shortener.open()
    link_shortener.input_link('https://pxl.leads.su/')
    link_shortener.button_click()
    link_shortener.checking_link('https://pxl.leads.su/')
