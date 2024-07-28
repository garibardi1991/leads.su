import allure
from pages.leads_pages import AuthenticationForm
from allure_commons.types import Severity
from pages.leads_pages import ShowcaseDesigner
from pages.leads_pages import LinkShortener


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
def test_showcase_designer(setup_browser_auto):
    with allure.step("Открытие конструктора витрин"):
        showcase_designer = ShowcaseDesigner()
        showcase_designer.open()

    with allure.step("Проверка нахождения витрины по ID в списке"):
        showcase_designer.check_showcase_id('2174')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Сокращатор ссылок")
@allure.story("Тестирование сокращатора ссылок")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_link_shortener(setup_browser_auto):
    with allure.step("Открытие сокращатора ссылок"):
        link_shortener = LinkShortener()
        link_shortener.open()

    with allure.step("Ввод сокращаемой ссылки"):
        link_shortener.input_link('https://pxl.leads.su/')

    with allure.step("Нажатие кнопки сократить"):
        link_shortener.button_click()

    with allure.step("Проверка что сократили данную ссылку"):
        link_shortener.checking_link('https://pxl.leads.su/')
