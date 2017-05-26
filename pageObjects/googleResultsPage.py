from browser import Browser
from selenium import webdriver
from pageObjects.basePage import BasePage
from elements.baseElement import BaseELement
from selenium.webdriver.common.by import By


class GoogleResultsPage(BasePage):

    result_stats = BaseELement(By.ID, "resultStats")
    URL = "www.google.pl/?q="

    def open(self):
        self.visit(self.URL)

    def get_number_of_results(self):
        result_string = self.result_stats.get_element().get_text()
        number_of_results = ""
        for s in result_string.split():
            if s.isdigit():
                number_of_results += s
            elif number_of_results != "":
                break

        return int(number_of_results)