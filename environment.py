from selenium import webdriver
import selectors.googlePage as googlePage
import selectors.googleResultsPage as googleResultsPage


def before_all(context):
  context.base_url = 'http://'
  context.driver = webdriver.Chrome('./chromedriver')
    
def after_all(context):  
  context.browser.close()