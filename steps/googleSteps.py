from time import sleep

class GoogleSteps(object):

    @given(u'I am on google page')
    def impl(context):
        context.google_page.open()
        sleep(1)

    @when(u'I search for {phrase}')
    def step_impl(context, phrase):
        context.google_page.fill_search_field(phrase)
        sleep(1)

    @when(u'I select {phrase} from search suggestions')
    def step_impl(context, phrase):
        context.google_page.select_search_suggestion(phrase)
        sleep(1)

    @then(u'I should see over {number:d} results')
    def imple(context, number):
        assert context.google_results_page.get_number_of_results() > number