'''LUXURY GIFT'''

import gift as base

class GiftLuxury(base.Gift):

    '''DERIVED CLASS'''

    def __init__(self, price, value, rating, difficulty):
        '''DEFAULT CONSTRUCTOR'''
        super(GiftLuxury, self).__init__(price, value)
        self.type = 'Luxury'
        self.rating = rating
        self.difficulty = difficulty
