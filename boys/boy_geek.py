'''GEEK BOY'''

from boys.boy import Boy

class BoyGeek(Boy):

    '''DEFAULT CONSTRUCTOR'''
    def __init__(self, name, attr, budget, intel, min_attr):
        super(BoyGeek, self).__init__(name, attr, budget, intel, min_attr)

    def set_happiness(self, gift_basket):
        '''CALCULATES HAPPINESS OF GEEK BOY'''
        self.happiness = self.partner.intel
