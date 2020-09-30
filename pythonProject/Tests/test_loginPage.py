from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Create_Account(BaseTest):

    def test_create_account(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.create_user()

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()
