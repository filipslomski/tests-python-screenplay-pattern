from selenium import webdriver

from abilities.ability import Ability

class BrowseTheWeb(Ability):

    def __init__(self, context):
        self.context = context

    def using(self, driver):
        if driver == 'chromedriver':
            self.context.driver = webdriver.Chrome('./chromedriver')