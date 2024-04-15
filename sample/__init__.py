from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'sample'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def store_values(self, pay, time, effect):
        self.pay = pay
        self.time = time
        self.effect = effect
        self.save()




# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['pay', 'time', 'effect']

    def vars_for_template(self):
        # Define dropdown options
        pay_choices = ['Option 1', 'Option 2', 'Option 3']
        time_choices = ['Option A', 'Option B', 'Option C']
        effect_choices = ['Choice X', 'Choice Y', 'Choice Z']

        return {
            'pay_choices': pay_choices,
            'time_choices': time_choices,
            'effect_choices': effect_choices
        }

    def before_next_page(self):
        # Print the stored variables to the console for debugging
        print("Stored variables - Pay: {}, Time: {}, Effect: {}".format(
            self.player.pay, self.player.time, self.player.effect
        ))




class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
