class BaseSteps(object):

    @given(u'a user visits the site')
    def impl(context):
        context.login_page.open()