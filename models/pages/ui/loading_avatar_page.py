from pathlib import Path

from selene import browser, have




class LoadingAvatar:
    def open(self):
        browser.open('account/user/update')

    def file_upload(self, file):
        browser.element('[type="file"]').send_keys(str(Path(__file__).parent.parent.joinpath(
            f'resources/{file}')))
    def click_save_button(self):
        browser.element('#save-btn').click()