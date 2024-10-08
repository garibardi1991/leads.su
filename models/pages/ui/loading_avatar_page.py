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
            with open(name, "wb") as file:
                response = requests.get(f'https://logo.s3.leads.su//197686/127170/:{name}')
                file.write(response.content)
        file_path = 'C:\\Users\\user\\PycharmProjects\\leads.su\\tests\\ui\\photo_2022-08-18_21-18-12.jpg'
        if os.path.exists(file_path):
            os.remove(file_path)

    def click_save_button(self):
        with allure.step("Сохрание профиля"):
            browser.element('#save-btn').click()


load_avatar = LoadingAvatar()
