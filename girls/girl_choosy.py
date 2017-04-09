'''CHOOSY GIRL'''

from girls.girl import Girl

class GirlChoosy(Girl):

    '''USES INHERITANCE'''

    def __init__(self, name, attr, mcost, intel, criteria):
        '''DEFAULT CONSTRUCTOR'''
        super(GirlChoosy, self).__init__(name, attr, mcost, intel, criteria)

    def set_happiness(self, gift_basket):
        '''CALCULATES HAPPINESS OF CHOOSY GIRL'''
        from math import log10
        from gifts.gift_luxury import GiftLuxury

        price_sum = sum(gift.price for gift in gift_basket) + \
                    sum(gift.price for gift in gift_basket if isinstance(gift, GiftLuxury))
        self.happiness = log10(price_sum)
