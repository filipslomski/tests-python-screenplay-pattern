class BaseStepsTwo(object):

    @when(u'I log in as {username}')
    def step_impl(context, username):
        context.login_page.login(username, "1234")

    @then(u'I should see the message {auth_message}')
    def imple(context, auth_message):
        assert context.login_page.get_login_message() == auth_message