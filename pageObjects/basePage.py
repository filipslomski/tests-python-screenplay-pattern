from browser import Browser
from selenium import webdriver


class BasePage(Browser):

    def element_with_argument(self, selector, argument):
        return selector.replace('{argument}', argument)