from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BaseELement(object):

    original_selector = ""
    selector = ""
    locator = By.ID
    element = None # type: WebElement

    def __init__(self, locator, selector):
        self.locator = locator
        self.original_selector = selector
        self.selector = selector

    def set_locator_parameter(self, argument):
        self.selector = self.original_selector.replace('{argument}', argument)

        return self

    def get_element(self):
        self.element = Browser.driver.find_element(self.locator, self.selector)

        return self

    def click(self):
        self.element.click()

    def set_value(self, value):
        self.element.send_keys(value)

    def is_element_visible(self):
        return self.element.is_displayed()

    def get_text(self):
        return self.element.text
