import os
import pytest


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from models.pages.ui.leads_auto_page import authentication_form
from utils import attach
from dotenv import load_dotenv

DEFAULT_BROWSER_VERSION = "100.0"

URL = 'https://webmaster.leads.su/'

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='122.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.base_url = 'https://webmaster.leads.su/'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.driver = driver
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

@pytest.fixture(scope='session')
def authorization (request):
    authentication_form.open()
    authentication_form.entering_login_password()
    authentication_form.check_id()
