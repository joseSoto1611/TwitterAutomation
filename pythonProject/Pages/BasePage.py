from lib2to3.pgen2 import driver

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


# This is the superclass where all the pages inherit methods

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # this method click any selected object
    def click(self, by_selector):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_selector)).click()

    # this method fills textboxes,textareas etc.
    def send_keys(self, by_selector, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_selector)).send_keys(text)

    # this method send keys and hit enter key
    def send_keys_enter(self, by_selector, text):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_selector))
        element.send_keys(text)
        element.submit()

    # this method checks if a particular element is visible in the UI
    def is_visible(self, by_selector):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_selector))
        return bool(element)

    # this method retuns the text within a object
    def get_element_text(self, by_selector):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_selector))
        return element.text

    # fill the dropdowns
    def fill_selector(self, by_selector, value):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_selector))
        select = Select(element)
        select.select_by_visible_text(value)
