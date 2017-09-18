from behave import *

from tasks.login_as import LoginAs
from tasks.open_web_page import OpenWebPage
from tasks.search_for_phrase import Search

credentials = {
    'A': ('filip.slomski@gmail.com', 'pass1'),
    'B': ('karol.slomski@gmail.com', 'pass2')
}

@given(u'I am on google page')
def impl(context):
    OpenWebPage(context).with_name('google_page').perform_as()

@when(u'I search for {phrase} then select {suggestion} from suggestions list')
def step_impl(context, phrase, suggestion):
    Search(context).for_phrase(phrase).then_select_from_search_suggestion(suggestion).perform_as()

@then(u'I should see over {number:d} results')
def imple(context, number):
    assert context.google_results_page.get_number_of_results() > number

@when(u'I login as user {username}')
def step_impl(context, username):
    LoginAs(context).perform_as()

@then(u'I should see user {username} as a logged user')
def imple(context, username):
    assert context.google_page.is_logged_user(credentials[username][0])