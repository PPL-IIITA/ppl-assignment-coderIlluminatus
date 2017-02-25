'''COUPLE'''

class Couple(object):

    '''COUPLE CLASS'''

    def __init__(self, boy, girl):
        '''DEFAULT CONSTRUCTOR'''
        self.boy = boy
        self.girl = girl
        self.happiness = 0
        self.compatibility = 0
        self.gift_basket = []

    def set_happiness(self):
        '''CALCULATES COUPLE'S HAPPINESS'''
        self.happiness = self.boy.happiness + self.girl.happiness

    def set_compatibility(self):
        '''CALCULATES COUPLE'S COMPATIBILITY'''
        money_diff = (self.boy.budget - self.girl.mcost)
        attr_diff = abs(self.boy.attr - self.girl.attr)
        intel_diff = abs(self.boy.intel - self.girl.intel)
        self.compatibility = money_diff + attr_diff + intel_diff
