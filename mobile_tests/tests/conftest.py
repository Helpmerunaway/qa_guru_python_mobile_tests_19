import os
from appium import webdriver
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def auto_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup():
    desired_caps = ({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
        'bstack:options': {
            "projectName": "Second Python project",
            "buildName": "browserstack-build-DEMO2",
            "sessionName": "BStack second_test"
        }
    })
    userName = os.getenv('userName')
    accessKey = os.getenv('accessKey')
    browser.config.driver = webdriver.Remote("http://" + str(userName) + ":" + str(accessKey) +
                                             "@hub-cloud.browserstack.com/wd/hub", desired_caps)
    browser.config.timeout = 4

