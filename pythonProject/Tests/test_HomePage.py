from Pages.HomePage import HomePage
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage


class Test_Twitter_Actions(BaseTest):

    # Those are the test cases based in homePage class
    def test_single_twitt(self):
        self.login = LoginPage(self.driver)
        self.login.login()
        self.homePage = HomePage(self.driver)
        self.homePage.twitt_text()

    def test_twitt_photo_text(self):
        self.login = LoginPage(self.driver)
        self.login.login()
        self.homePage = HomePage(self.driver)
        self.homePage.twitt_photo_Text()

    def test_twitt_video_text(self):
        self.login = LoginPage(self.driver)
        self.login.login()
        self.homePage = HomePage(self.driver)
        self.homePage.twitt_video_text()

    def test_twitt_link(self):
        self.login = LoginPage(self.driver)
        self.login.login()
        self.homePage = HomePage(self.driver)
        self.homePage.twitt_link()
