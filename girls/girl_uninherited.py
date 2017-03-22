'''GIRL'''

class Girl(object):

    '''DOES NOT USE INHERITANCE'''

    def __init__(self, name, attr, mcost, intel, nature, criteria):
        self.name = name
        self.attr = attr
        self.mcost = mcost
        self.intel = intel
        self.status = 'Single'
        self.nature = nature
        self.partner = None
        self.happiness = 0
        self.criteria = criteria

    def check_elligibility(self, boy):
        '''CHECKS WHETHER THIS BOY IS ELIGIBLE FOR PAIRING WITH THE CURRENT GIRL'''
        if self.mcost <= boy.budget:
            return True
        return False

    def match(self, boy):
        '''ASSIGNS BOY AS THE PARTNER FOR THIS GIRL'''
        self.status = 'Committed'
        self.partner = boy

    def set_happiness(self, gift_basket):
        '''CALCULATES HAPPINESS OF THIS GIRL'''
        from math import exp, log10

        price_sum, value_sum = 0, 0
        for gift in gift_basket:
            if self.nature != 'Desparate':
                value_sum += gift.value
            if self.nature == 'Choosy' and gift.nature == 'Luxury':
                price_sum += gift.price * 2
            else:
                price_sum += gift.price

        if self.nature == 'Choosy':
            self.happiness = log10(price_sum)
        elif self.nature == 'Normal':
            self.happiness = price_sum + value_sum
        elif self.nature == 'Desparate':
            self.happiness = exp(price_sum)
