from pathlib import Path

import allure
from selene import browser


class LoadingAvatar:
    def open(self):
        with allure.step("Открыть профиль пользователя"):
            browser.open('account/user/update')

    def file_upload(self, file):
        with allure.step("Загрузка изображения"):
            browser.element('[type="file"]').send_keys(str(Path(__file__).parent.parent.joinpath(
                f'{file}')))

    def click_save_button(self):
        with allure.step("Сохрание профиля"):
            browser.element('#save-btn').click()


load_avatar = LoadingAvatar()
