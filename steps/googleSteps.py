from behave import *

from tasks.login_as import LoginAs
from tasks.open_web_page import OpenWebPage
from tasks.search_for_phrase import Search
from questions.get_logged_user import GetLoggedUser
from stage import Stage

stage = Stage()

@given(u'{actor} is on google page')
def impl(context, actor):
    OpenWebPage(context).with_name('google_page').perform_as(stage.call_to_stage_for(actor))

@when(u'he searches for {phrase} then select {suggestion} from suggestions list')
def step_impl(context, phrase, suggestion):
    Search(context).for_phrase(phrase).then_select_from_search_suggestion(suggestion).perform_as(
        stage.the_actor_in_the_spotlight())

@then(u'he should see over {number:d} results')
def imple(context, number):
    assert context.google_results_page.get_number_of_results() > number

@when(u'{actor} logs in')
def step_impl(context, actor):
    stage.call_to_stage_for(actor)
    LoginAs(context).perform_as(stage.the_actor_in_the_spotlight())

@then(u'he should see himself as a logged user')
def imple(context):
    assert GetLoggedUser(context).perform_as(
        stage.the_actor_in_the_spotlight()) == stage.the_actor_in_the_spotlight().email