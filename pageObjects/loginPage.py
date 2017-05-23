from browser import Browser
from selenium import webdriver


class LoginPage(Browser):

    username_field = ""
    password_field = ""
    submit_button = ""
    auth_message = ""

    def __init__(self):
        self.username_field = "username"
        self.password_field = "password"
        self.submit_button = "submit"
        self.auth_message = "auth-message"
        self.LOGIN = '/'

    def open(self):
        self.visit(self.LOGIN)

    def login(self, username, password):
        self.open()
        self.find_by_id(self.username_field).send_keys(username)
        self.find_by_id(self.password_field).send_keys(password)
        self.find_by_id(self.submit_button).click()

    def get_login_message(self):
        auth_message = self.find_by_id(self.auth_message)

        return auth_message.text
