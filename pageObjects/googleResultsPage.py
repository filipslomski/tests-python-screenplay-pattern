from browser import Browser
from selenium import webdriver
from pageObjects.basePage import BasePage
import re


class GoogleResultsPage(BasePage):

    result_stats = "resultStats"
    URL = "www.google.pl/?q="

    def open(self):
        self.visit(self.URL)

    def get_number_of_results(self):
        result_string = self.find_by_id(self.result_stats).text
        number_of_results = ""
        for s in result_string.split():
            if s.isdigit():
                number_of_results += s
            elif number_of_results != "":
                break

        return int(number_of_results)