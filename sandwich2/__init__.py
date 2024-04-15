from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'sandwich'
    players_per_group = None
    num_rounds = 12


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    orders_submitted = models.IntegerField(initial=0)
    total_errors = models.IntegerField(initial=0)
    average_errors = models.FloatField(initial=0.0)
    orders_redone = models.IntegerField(initial=0)


def round_number(self):
    return self.round_number


# PAGES
class MyPage(Page):
    form_model = 'player'
    timeout_seconds = 25

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'orders_submitted': player.orders_submitted,
            'total_errors': player.total_errors,
            'average_errors': player.average_errors,
            'orders_redone': player.orders_redone,
        }






class ResultsWaitPage(WaitPage):
    pass


class Feedback(Page):
    def vars_for_template(player: Player):
        return {
            'orders_submitted': player.orders_submitted,
            'total_errors': player.total_errors,
            'average_errors': player.average_errors,
            'orders_redone': player.orders_redone,
        }




page_sequence = [MyPage, Feedback]
