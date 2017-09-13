@when(u'I select {phrase} from search suggestions')
def step_impl(context, phrase):
    context.google_page.select_search_suggestion(phrase)