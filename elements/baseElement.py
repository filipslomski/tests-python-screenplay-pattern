from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):

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
        self.element = WebDriverWait(Browser.driver, 3).until(
            EC.presence_of_element_located((self.locator, self.selector))
        )

        return self

    def click(self):
        self.element.click()

    def set_value(self, value):
        self.element.send_keys(value)

    def is_element_visible(self, timeout = 5):
        is_visible = WebDriverWait(Browser.driver, timeout).until(
            EC.visibility_of_element_located((self.locator, self.selector))
        )
        return False if is_visible == False else True

    def is_element_present(self, timeout):
        is_present = WebDriverWait(Browser.driver, timeout).until(
            EC.presence_of_element_located((self.locator, self.selector))
        )
        return False if is_present == False else True

    def is_element_visible_now(self):
        return self.element.is_displayed()

    def is_element_present_now(self):
        return self.is_element_present(0)

    def get_text(self):
        return self.element.text
