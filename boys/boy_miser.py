'''MISER BOY'''

from boys.boy import Boy

class BoyMiser(Boy):

    '''DEFAULT CONSTRUCTOR'''
    def __init__(self, name, attr, budget, intel, min_attr):
        super(BoyMiser, self).__init__(name, attr, budget, intel, min_attr)

    def set_happiness(self, gift_basket):
        '''CALCULATES HAPPINESS OF MISER BOY'''
        self.happiness = self.budget - sum(gift.price for gift in gift_basket)
