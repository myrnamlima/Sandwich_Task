from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'sandwich'
    players_per_group = None
    num_rounds = 4


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    orders_submitted = models.IntegerField(initial=0)
    total_errors = models.IntegerField(initial=0)
    average_errors = models.FloatField(initial=0.0)
    orders_redone = models.IntegerField(initial=0)
    orders_zero_mistakes = models.IntegerField(initial=0)
    orders_one_mistake = models.IntegerField(initial=0)
    orders_two_mistakes = models.IntegerField(initial=0)
    orders_three_mistakes = models.IntegerField(initial=0)


def round_number(self):
    return self.round_number


# PAGES
class MyPage(Page):
    form_model = 'player'
    timeout_seconds = 25

    @staticmethod
    def live_method(player, data):
        # Process the received data
        # For example, you can store it in the database
        player.orders_submitted = data['ordersSubmitted']
        player.total_errors = data['totalErrors']
        player.average_errors = data['averageErrors']
        player.orders_redone = data['ordersRedone']
        player.orders_zero_mistakes = data['ordersZeroMistakes']
        player.orders_one_mistake = data['ordersOneMistake']
        player.orders_two_mistakes = data['ordersTwoMistakes']
        player.orders_three_mistakes = data['ordersThreeMistakes']






class ResultsWaitPage(WaitPage):
    pass


class Feedback(Page):
    def live_method(player, data):
        # Update player attributes with the received data
        player.orders_submitted = data['ordersSubmitted']
        player.total_errors = data['totalErrors']
        player.average_errors = data['averageErrors']
        player.orders_redone = data['ordersRedone']
        player.orders_zero_mistakes = data['ordersZeroMistakes']
        player.orders_one_mistake = data['ordersOneMistake']
        player.orders_two_mistakes = data['ordersTwoMistakes']
        player.orders_three_mistakes = data['ordersThreeMistakes']

        def vars_for_template(player: Player):
            return {
                'orders_submitted': player.orders_submitted,
                'total_errors': player.total_errors,
                'average_errors': player.average_errors,
                'orders_redone': player.orders_redone,
                'orders_zero_mistakes': player.orders_zero_mistakes,
                'orders_one_mistake': player.orders_one_mistake,
                'orders_two_mistakes': player.orders_two_mistakes,
                'orders_three_mistakes': player.orders_three_mistakes,
            }




page_sequence = [MyPage, Feedback]
