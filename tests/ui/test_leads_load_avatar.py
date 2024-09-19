import allure
from allure_commons.types import Severity
from models.pages.ui.loading_avatar_page import load_avatar


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Загрузка аватара пользователя")
@allure.story("Тестирование загрузки аватара пользователя")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_load_avatar():
    load_avatar.open()
    load_avatar.file_upload('photo_2022-08-18_21-18-12.jpg')
    load_avatar.checking_file('photo_2022-08-18_21-18-12.jpg')
    load_avatar.click_save_button()
