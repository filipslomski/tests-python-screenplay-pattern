from browser import Browser
from selenium import webdriver
import pageObjects.loginPage as loginPage
import pageObjects.googlePage as googlePage
import pageObjects.googleResultsPage as googleResultsPage


def before_all(context):
  context.browser = Browser()
  context.login_page = loginPage.LoginPage()
  context.google_page = googlePage.GooglePage()
  context.google_results_page = googleResultsPage.GoogleResultsPage()

    
def after_all(context):  
  context.browser.close()