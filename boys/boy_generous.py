'''GENEROUS BOY'''

from boys.boy import Boy

class BoyGenerous(Boy):

    '''DEFAULT CONSTRUCTOR'''
    
    def __init__(self, name, attr, budget, intel, min_attr):
        super(BoyGenerous, self).__init__(name, attr, budget, intel, min_attr)

    def set_happiness(self, gift_basket):
        '''CALCULATES HAPPINESS OF GENEROUS BOY'''
        self.happiness = self.partner.happiness
