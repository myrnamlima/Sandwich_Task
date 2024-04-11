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
    ordersSubmitted = models.IntegerField(initial=0)
    totalErrors = models.IntegerField(initial=0)
    averageErrors = models.FloatField(initial=0.0)
    ordersRedone = models.IntegerField(initial=0)

    def js_vars(player):
        return dict(
            ordersSubmitted=player.ordersSubmitted,
            totalErrors=player.totalErrors,
            averageErrors=player.averageErrors,
            ordersRedone=player.ordersRedone,
        )


# PAGES
class MyPage(Page):
    form_model = 'player'
    timeout_seconds = 20




class ResultsWaitPage(WaitPage):
    pass


class Feedback(Page):
    pass




page_sequence = [MyPage, Feedback]
