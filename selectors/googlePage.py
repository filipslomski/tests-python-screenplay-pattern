from selectors.basePage import BasePage
from elements.element import Element
from selenium.webdriver.common.by import By


class GooglePage(BasePage):

    URL = 'www.google.pl'

    def __init__(self, context):
        self.search_field = Element(By.ID, "lst-ib", context)
        self.search_suggestion = Element(By.XPATH, ".//ul[@role='listbox']/li//div[string(.)='{argument}']", context)
        self.sign_in = Element(By.XPATH, ".//a[@id='gb 70']", context)
        self.password_field = Element(By.XPATH, ".//input[@name='password']", context)
        self.email_field = Element(By.XPATH, "", context)
        self.login_next_button = Element(By.XPATH, ".//*[text()='Next']", context)
        self.logged_user_icon = Element(By.XPATH, ".//span[@id='gb_7a']", context)
        self.logged_user_email_info = Element(By.XPATH, ".//*[contains(@class,'gb_xb')]", context)
        super().__init__(context)
