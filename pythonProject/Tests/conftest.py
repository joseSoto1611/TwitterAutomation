import pytest
from selenium import webdriver
from Config.Config import TestData


# this is the set up of the web driver excecutable_path must be changed to host path

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    web_driver = webdriver.Chrome(executable_path="D:\\drivers\\chromedriver.exe")
    request.cls.driver = web_driver
    web_driver.get(TestData.BASE_URL)
    web_driver.maximize_window()
    web_driver.implicitly_wait(5)

    yield
    web_driver.close()
