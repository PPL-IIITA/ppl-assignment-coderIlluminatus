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

    def get_boy_nature(self):
        if(hasattr(self.boy, 'nature')):
            return self.boy.nature
        else:
            return type(self.boy).__name__[3:]

    def get_girl_nature(self):
        if(hasattr(self.girl, 'nature')):
            return self.girl.nature
        else:
            return type(self.girl).__name__[4:]


    def set_happiness(self):
        '''CALCULATES COUPLE'S HAPPINESS'''
        self.happiness = self.boy.happiness + self.girl.happiness

    def set_compatibility(self):
        '''CALCULATES COUPLE'S COMPATIBILITY'''
        money_diff = (self.boy.budget - self.girl.mcost)
        attr_diff = abs(self.boy.attr - self.girl.attr)
        intel_diff = abs(self.boy.intel - self.girl.intel)
        self.compatibility = money_diff + attr_diff + intel_diff

    def break_up(self):
        print(self.girl.name + '\t  AND\t' + self.boy.name + '\tHAPPINESS    \t=\t' + str(self.happiness))
        self.boy.break_up()
        self.girl.break_up()
        self.gift_basket = []
