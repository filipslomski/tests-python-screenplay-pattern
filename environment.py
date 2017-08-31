from selenium import webdriver
import pageObjects.googlePage as googlePage
import pageObjects.googleResultsPage as googleResultsPage


def before_all(context):
  context.base_url = 'http://'
  context.driver = webdriver.Chrome('./chromedriver')

  context.google_page = googlePage.GooglePage(context)
  context.google_results_page = googleResultsPage.GoogleResultsPage(context)

    
def after_all(context):  
  context.browser.close()