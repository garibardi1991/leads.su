import allure
import json
import logging

from allure_commons.types import AttachmentType
from curlify import to_curl
from requests import Response

def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')


# def response_logging(response: Response):
#     logging.info("Request: " + response.request.url)
#
#     if response.request.body:
#         request_body = response.request.body.decode('utf-8')
#         logging.info("INFO Request body: " + request_body)
#
#     logging.info("Request headers: " + str(response.request.headers))
#     logging.info("Response code: " + str(response.status_code))
#     logging.info("Response: " + response.text)
#
#
# def request_attaching(response: Response):
#     with allure.step(f'{response.request.method} {response.request.url}'):
#         curl = to_curl(response.request)
#         logging.info(curl)
#         logging.info(f'status code: {response.status_code}')
#         allure.attach(body=curl, name='curl', attachment_type=allure.attachment_type.TEXT, extension='txt')
#
#
# def response_attaching(response: Response):
#     allure.attach(
#         body=response.request.url,
#         name="Request url",
#         attachment_type=AttachmentType.TEXT,
#     )
#
#     if response.request.body:
#         allure.attach(
#             body=response.request.body.decode('utf-8') if response.request.body else None,
#             name="Request body",
#             attachment_type=AttachmentType.JSON,
#             extension="json",
#         )
#         allure.attach(
#             body=json.dumps(response.json(), indent=4, ensure_ascii=True),
#             name="Response",
#             attachment_type=AttachmentType.JSON,
#             extension="json",
#         )