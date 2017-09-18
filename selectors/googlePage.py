from selectors.basePage import BasePage
from elements.element import Element
from selenium.webdriver.common.by import By


class GooglePage(BasePage):

    URL = 'www.google.pl'

    search_field = Element(By.ID, "lst-ib", context)
    search_suggestion = Element(By.XPATH, ".//ul[@role='listbox']/li//div[string(.)='{argument}']", context)
    sign_in = Element(By.XPATH, ".//a[@id='gb 70']", context)
    password_field = Element(By.XPATH, ".//input[@name='password']", context)
    email_field = Element(By.XPATH, "", context)
    login_next_button = Element(By.XPATH, ".//*[text()='Next']", context)
    logged_user_icon = Element(By.XPATH, ".//span[@id='gb_7a']", context)
    logged_user_email_info = Element(By.XPATH, ".//*[contains(@class,'gb_xb')]", context)

    def __init__(self, context):
        super().__init__(context)
