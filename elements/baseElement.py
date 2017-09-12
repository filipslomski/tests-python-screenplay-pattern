"""
BaseElement
"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseElement(object):
    """Base element class contains all the common methods & attributes
    inherited by other elements
    """
    selector = ""
    locator = By.ID
    elements_collection = []
    element = None

    def __init__(self, locator, selector, context):
        self.locator = locator
        self.original_selector = selector
        self.selector = selector
        self.browser = context.browser
        self.context = context

    @property
    def element(self):
        """Use selenium wait in order to retrieve actual WebElement from DOM

        :return: WebElement
        """
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((self.locator, self.selector))
        )

    def set_parameters(self, *args):
        """Takes a single string or an array of strings and add them as parameters
        to selector string.
        I.e:
        set_parameters(['a', 'b']) for selector ".//[{}][{}]" will set selector to
        ".//['a']['b']"

        :param args: string|[string]
        :return: self
        """
        self.selector = self.original_selector.format(*args)

        return self

    def mouse_hover(self):
        """Hover the mouse over element

        :return: None
        """
        webdriver.ActionChains(self.browser).move_to_element(self.element).perform()

    def get_elements(self):
        """Retrieves actual WebElements from DOM, saves them in an array and returns

        :return: [WebElement]
        """
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((self.locator, self.selector))
        )
        self.elements_collection = self.browser.find_elements(self.locator, self.selector)

        return self.elements_collection

    def click(self):
        """Clicks the element

        :return: None
        """
        self.element.click()

    def get_attribute(self, name):
        """Returns element attribute value

        :param name: string
        :return: string
        """
        return self.element.get_attribute(name)

    @property
    def value(self):
        """Returns the content of "value" attribute

        :return: string
        """
        return self.element.get_attribute('value')

    @value.setter
    def value(self, value):
        """Sets value for element (i.e. textField)

        :param value: string
        :return: None
        """
        self.element.clear()
        self.element.send_keys(value)

    def is_element_visible(self, timeout=7):
        """Checks if element is visible by selenium within given timeout

        :param timeout: int
        :return: boolean
        """
        try:
            is_visible = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located((self.locator, self.selector))
            )
        except TimeoutException:
            is_visible = False

        return bool(is_visible)

    def is_element_not_visible(self, timeout=7):
        """Checks if elements is not visible by selenium within given timeout

        :param timeout: int
        :return: boolean
        """
        try:
            is_invisible = WebDriverWait(self.browser, timeout).until(
                EC.invisibility_of_element_located((self.locator, self.selector))
            )
        except TimeoutException:
            is_invisible = False

        return is_invisible

    def is_element_present(self, timeout=3):
        """Checks if element is present by selenium within given timeout

        :param timeout: int
        :return: boolean
        """
        try:
            is_present = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((self.locator, self.selector))
            )
        except TimeoutException:
            is_present = False

        return bool(is_present)

    def is_element_visible_now(self):
        """Checks if element is visible at this moment

        :return: boolean
        """
        return self.element.is_displayed()

    def is_element_present_now(self):
        """Checks if element is present at this moment

        :return: boolean
        """
        return self.is_element_present(1)

    @property
    def text(self):
        """Returns element's text if selenium can handle it well

        :return: string
        """
        return self.element.text
