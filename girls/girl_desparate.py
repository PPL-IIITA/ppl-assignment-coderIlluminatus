'''DESPARATE GIRL'''

from girls.girl import Girl

class GirlDesparate(Girl):

    '''USES INHERITANCE'''

    def __init__(self, name, attr, mcost, intel, criteria):
        '''DEFAULT CONSTRUCTOR'''
        super(GirlDesparate, self).__init__(name, attr, mcost, intel, criteria)

    def set_happiness(self, gift_basket):
        '''CALCULATES HAPPINESS OF DESPARATE GIRL'''
        from math import exp

        price_sum = sum(gift.price for gift in gift_basket)
        self.happiness = exp(price_sum)
