from browser import Browser
from selenium import webdriver
import pageObjects.basePage as basePage
from pageObjects.basePage import BasePage
from elements.baseElement import BaseELement
from selenium.webdriver.common.by import By


class GooglePage(BasePage):

    search_field = BaseELement(By.ID, "lst-ib")
    search_suggestion = BaseELement(By.XPATH, ".//ul[@role='listbox']/li//div[string(.)='{argument}']")
    URL = 'www.google.pl'

    def open(self):
        self.visit(self.URL)

    def fill_search_field(self, search_phrase):
        self.search_field.get_element().set_value(search_phrase)

    def select_search_suggestion(self, suggestion):
        self.search_suggestion.set_locator_parameter(suggestion).get_element().click()