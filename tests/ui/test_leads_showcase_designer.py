import allure
from allure_commons.types import Severity
from models.pages.ui.designer_page import showcase_designer



@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Отображение витрины")
@allure.story("Тестирование отображения витрины в конструкторе")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_showcase_designer(authorization):
    showcase_designer.open()
    showcase_designer.check_showcase_id('3324')
