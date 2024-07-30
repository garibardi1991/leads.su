import allure
from models.pages.ui.leads_auto_page import authentication_form
from allure_commons.types import Severity
from models.pages.ui.designer_page import showcase_designer
from models.pages.ui.shortener_page import link_shortener
from models.pages.ui.loading_avatar_page import load_avatar
from models.pages.ui.home_scroll_page import home_page_scroll


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


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Отображение витрины")
@allure.story("Тестирование отображения витрины в конструкторе")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_showcase_designer():
    showcase_designer.open()
    showcase_designer.check_showcase_id('2174')


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


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Загрузка аватара пользователя")
@allure.story("Тестирование загрузки аватара пользователя")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_load_avatar():
    load_avatar.open()
    load_avatar.file_upload('photo_2022-08-18_21-18-12.jpg')
    load_avatar.checking_file()
    load_avatar.click_save_button()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Работа скролла на главной странице")
@allure.story("Тестирование работы скролла")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_scrolling_home_page():
    home_page_scroll.open()
    home_page_scroll.check_scroll_offers('Офферы специально для вас')
    home_page_scroll.check_scroll_id('ID 197686')
