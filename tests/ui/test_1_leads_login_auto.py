import allure
from models.pages.ui.leads_auto_page import authentication_form
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Авторизация на ЛКВ")
@allure.story("Тестирование формы авторизации на ЛКВ")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_login_auto(setup_browser):
    authentication_form.open()
    authentication_form.entering_login_password()
    authentication_form.check_id()
