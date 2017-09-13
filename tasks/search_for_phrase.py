from tasks.task import Task

class Search(Task):
    pass

@when(u'I search for {phrase}')
def step_impl(context, phrase):
    context.google_page.fill_search_field(phrase)