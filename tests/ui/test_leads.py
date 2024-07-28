import allure
from models.pages.ui.leads_auto_page import AuthenticationForm
from allure_commons.types import Severity
from models.pages.ui.designer_page import ShowcaseDesigner
from models.pages.ui.shortener_page import LinkShortener
from models.pages.ui.loading_avatar_page import LoadingAvatar
from models.pages.ui.scroll_page import PageScroll


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
        authentication_form.entering_login_password()

    with allure.step("Проверяем, что вошли под тем пользователем"):
        authentication_form.check_id()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Отображение витрины")
@allure.story("Тестирование отображения витрины в конструкторе")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_showcase_designer():
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
def test_link_shortener():
    with allure.step("Открытие сокращатора ссылок"):
        link_shortener = LinkShortener()
        link_shortener.open()

    with allure.step("Ввод сокращаемой ссылки"):
        link_shortener.input_link('https://pxl.leads.su/')

    with allure.step("Нажатие кнопки сократить"):
        link_shortener.button_click()

    with allure.step("Проверка что сократили данную ссылку"):
        link_shortener.checking_link('https://pxl.leads.su/')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Загрузка аватара пользователя")
@allure.story("Тестирование загрузки аватара пользователя")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_load_avatar():
    with allure.step("Открыть профиль пользователя"):
        load_avatar = LoadingAvatar()
        load_avatar.open()

    with allure.step("Загрузка изображения"):
        load_avatar.file_upload('photo_2022-08-18_21-18-12.jpg')

    with allure.step("Сохрание профиля"):
        load_avatar.click_save_button()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Работа скролла на главной странице")
@allure.story("Тестирование работы скролла")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_link_shortener():
    with allure.step("Открыть главную страницу"):
        page_scroll = PageScroll()
        page_scroll.open()

    with allure.step("Скролл до 'Офферы специально для вас'"):
        page_scroll.check_scroll_offers('Офферы специально для вас')

    with allure.step("Скролл до ID пользователя"):
        page_scroll.check_scroll_id('ID 197686')
