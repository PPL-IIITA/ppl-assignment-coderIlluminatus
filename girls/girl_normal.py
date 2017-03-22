'''NORMAL GIRL'''

from girls.girl import Girl

class GirlNormal(Girl):

    '''USES INHERITANCE'''

    def __init__(self, name, attr, mcost, intel, criteria):
        '''DEFAULT CONSTRUCTOR'''
        super(GirlNormal, self).__init__(name, attr, mcost, intel, criteria)

    def set_happiness(self, gift_basket):
        '''CALCULATES HAPPINESS OF NORMAL GIRL'''
        price_sum = sum(gift.price for gift in gift_basket)
        value_sum = sum(gift.value for gift in gift_basket)
        self.happiness = price_sum + value_sum
