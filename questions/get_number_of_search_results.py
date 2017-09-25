from questions.question import Question
from interactions.get import Get


class GetNumberOfSearchResults(Question):

    def __init__(self, context):
        self.context = context
        super().__init__(context)

    def perform_as(self, actor):

        return actor.attempts_to(
            self.__get_results_number(
                Get(self.context).text().from_element(self.context.google_page.logged_user_email_info)
            )
        )

    def __get_results_number(self, result_stats):
        number_of_results = ""
        for s in result_stats.split():
            if s.isdigit():
                number_of_results += s
            elif number_of_results != "":
                break

        return int(number_of_results)