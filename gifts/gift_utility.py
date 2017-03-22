'''LUXURY GIFT'''

from gifts.gift import Gift

class GiftUtility(Gift):

    '''DERIVED CLASS'''

    def __init__(self, name, price, value, util_value, util_class):
        '''DEFAULT CONSTRUCTOR'''
        super(GiftUtility, self).__init__(name, price, value)
        self.util_value = util_value
        self.util_class = util_class
