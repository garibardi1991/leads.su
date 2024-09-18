import allure
from allure_commons.types import Severity
from models.pages.ui.home_page import home_page


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Работа скролла на главной странице")
@allure.story("Тестирование работы скролла")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_scrolling_home_page(authorization):
    home_page.open()
    home_page.check_scroll_offers('Офферы специально для вас')
    home_page.check_scroll_id('ID 197686')
