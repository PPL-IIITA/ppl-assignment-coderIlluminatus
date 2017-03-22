'''LUXURY GIFT'''

from gifts.gift import Gift

class GiftLuxury(Gift):

    '''DERIVED CLASS'''

    def __init__(self, name, price, value, rating, difficulty):
        '''DEFAULT CONSTRUCTOR'''
        super(GiftLuxury, self).__init__(name, price, value)
        self.rating = rating
        self.difficulty = difficulty
