from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage


class HomePage(BasePage):

    # Action Selectors

    btn_twittear = (By.XPATH, '//select[@aria-label=\'Twittear\']')
    txt_area = (By.XPATH, '//select[@aria-label=\'Texto del Tweet\']')
    btn_add_image = (By.XPATH, '//select[@aria-label=\'Agregar fotos o video\']')
    btn_atras = (By.XPATH, '//select[@aria-label=\'Atrás\']')

    #class constructor

    def __init__(self, driver):
        super().__init__(driver)

        #this method creates a Single twitt

    def twitt_text(self):
        self.click(self.btn_atras)
        self.click(self.txt_area)
        self.send_keys_enter(self.txt_area, "This is a single Test")
       # self.click(self.btn_twittear)

    #this methods adds photos or Videos

    def twitt_photo_Text(self):
        self.click(self.btn_atras)
        self.click(self.txt_area)
        self.send_keys_enter(self.txt_area, "This is a single Test")
        self.send_keys_enter(self.btn_add_image, "insert path")
        # self.click(self.btn_twittear)

    def twitt_video_text(self):
        self.click(self.btn_atras)
        self.click(self.txt_area)
        self.send_keys_enter(self.txt_area, "This is a single Test")
        self.send_keys_enter(self.btn_add_image, "insert path")
        # self.click(self.btn_twittear)

    # this method post a Link

    def twitt_link(self):
        self.click(self.btn_atras)
        self.click(self.txt_area)
        self.send_keys_enter(self.txt_area, "insert Link to post")
        #self.click(self.btn_twittear)