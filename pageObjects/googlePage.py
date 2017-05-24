from browser import Browser
from selenium import webdriver
import pageObjects.basePage as basePage
from pageObjects.basePage import BasePage


class GooglePage(BasePage):

    search_field = "lst-ib"
    search_suggestion = ".//ul[@role='listbox']/li//div[string(.)='{argument}']"
    URL = 'www.google.pl'

    def open(self):
        self.visit(self.URL)

    def fill_search_field(self, search_phrase):
        self.find_by_id(self.search_field).send_keys(search_phrase)

    def select_search_suggestion(self, suggestion):
        self.find_by_xpath(self.element_with_argument(self.search_suggestion, suggestion)).click()