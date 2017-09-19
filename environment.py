import selectors.googlePage as googlePage
import selectors.googleResultsPage as googleResultsPage


def before_all(context):
  context.base_url = 'http://'

  context.google_page = googlePage.GooglePage(context)
  context.google_results_page = googleResultsPage.GoogleResultsPage(context)


def after_all(context):  
  context.browser.close()