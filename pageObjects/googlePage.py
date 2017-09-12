from pageObjects.basePage import BasePage
from elements.element import Element
from selenium.webdriver.common.by import By


class GooglePage(BasePage):

    URL = 'www.google.pl'

    def __init__(self, context):
        super().__init__(context)
        self.search_field = Element(By.ID, "lst-ib", context)
        self.search_suggestion = Element(By.XPATH, ".//ul[@role='listbox']/li//div[string(.)='{argument}']", context)
        self.sign_in = Element(By.XPATH, ".//a[@id='gb 70']", context)
        self.password_field = Element(By.XPATH, ".//input[@name='password']", context)
        self.email_field = Element(By.XPATH, "", context)
        self.login_next_button = Element(By.XPATH, ".//*[text()='Next']", context)
        self.logged_user_icon = Element(By.XPATH, ".//span[@id='gb_7a']", context)
        self.logged_user_email_info = Element(By.XPATH, ".//*[contains(@class,'gb_xb')]", context)

    def fill_search_field(self, search_phrase):
        self.search_field.value = search_phrase

    def select_search_suggestion(self, suggestion):
        self.search_suggestion.set_parameters(suggestion).click()

    def login_as(self, email, password):
        self.email_field.value = email
        self.password_field.value = password
        self.login_next_button.click()

    def is_logged_user(self, name):
        self.logged_user_icon.click()
        return self.logged_user_email_info.text == name
