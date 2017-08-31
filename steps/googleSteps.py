from behave import *

credentials = {
    'A': ('filip.slomski@gmail.com', 'pass1'),
    'B': ('karol.slomski@gmail.com', 'pass2')
}

@given(u'I am on google page')
def impl(context):
    context.google_page.open()

@when(u'I search for {phrase}')
def step_impl(context, phrase):
    context.google_page.fill_search_field(phrase)

@when(u'I select {phrase} from search suggestions')
def step_impl(context, phrase):
    context.google_page.select_search_suggestion(phrase)

@then(u'I should see over {number:d} results')
def imple(context, number):
    assert context.google_results_page.get_number_of_results() > number

@when(u'I login as user {username}')
def step_impl(context, username):
    context.google_page.login_as(credentials[username][0], credentials[username][1])

@then(u'I should see user {username} as a logged user')
def imple(context, username):
    assert context.google_page.is_logged_user(credentials[username][0])