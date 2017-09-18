from selectors.basePage import BasePage
from elements.element import Element
from selenium.webdriver.common.by import By


class GoogleResultsPage(BasePage):

    URL = "www.google.pl/?q="

    result_stats = Element(By.ID, "resultStats", context)

    def __init__(self, context):
        super().__init__(context)


    def get_number_of_results(self):
        result_string = self.result_stats.text
        number_of_results = ""
        for s in result_string.split():
            if s.isdigit():
                number_of_results += s
            elif number_of_results != "":
                break

        return int(number_of_results)