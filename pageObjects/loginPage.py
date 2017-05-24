from browser import Browser
from selenium import webdriver
from pageObjects.basePage import BasePage


class LoginPage(BasePage):

    username_field = "username"
    password_field = "password"
    submit_button = "submit"
    auth_message = "auth-message"
    URL = '/'

    def open(self):
        self.visit(self.URL)

    def login(self, username, password):
        self.open()
        self.find_by_id(self.username_field).send_keys(username)
        self.find_by_id(self.password_field).send_keys(password)
        self.find_by_id(self.submit_button).click()

    def get_login_message(self):
        auth_message = self.find_by_id(self.auth_message)

        return auth_message.text
