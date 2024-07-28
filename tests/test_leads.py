import allure
from pages.leads_pages import AuthenticationForm
from allure_commons.types import Severity
from pages.leads_pages import ShowcaseDesigner

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Авторизация на ЛКВ")
@allure.story("Тестирование формы авторизации на ЛКВ")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_login_auto(setup_browser):

    with allure.step("Открытие регистрационной формы"):
        authentication_form = AuthenticationForm()
        authentication_form.open()

    with allure.step("Вводим логин и пароль"):
        authentication_form.type_log_pass()

    with allure.step("Проверяем, что вошли под тем пользователем"):
        authentication_form.check_id()

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Отображение витрины")
@allure.story("Тестирование отображения витрины в конструкторе")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_login_auto(setup_browser):
    with allure.step("Открытие констурктора витрин"):
        showcase_designer= ShowcaseDesigner()
        showcase_designer.open()

    with allure.step("Проверка находжения витрины по ID в списке"):
        showcase_designer.check_showcase_id('2174')







