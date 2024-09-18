import os

import allure
import requests
from selene import browser

from utils import resource


class LoadingAvatar:
    def open(self):
        with allure.step("Открыть профиль пользователя"):
            browser.open('account/user/update')

    def file_upload(self, file):
        with allure.step("Загрузка изображения"):
            browser.element('[type="file"]').set_value(resource.path(file))

    def checking_file(self, name):
        with allure.step("Проверяем загруженное изображение"):
            file_path = name
            response = requests.get(f'https://logo.s3.leads.su//197686/127170/:{name}')
            response.raise_for_status()
            with open(file_path, "wb") as file:
                file.write(response.content)
        self.cleanup(file_path)

    def cleanup(self, file_path):
        with allure.step("Удаляем загруженный файл"):
            if os.path.exists(file_path):
                os.remove(file_path)

    def click_save_button(self):
        with allure.step("Сохрание профиля"):
            browser.element('#save-btn').click()


load_avatar = LoadingAvatar()
