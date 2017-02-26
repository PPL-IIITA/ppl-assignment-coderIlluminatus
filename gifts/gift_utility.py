'''LUXURY GIFT'''

import gift as base

class GiftUtility(base.Gift):

    '''DERIVED CLASS'''

    def __init__(self, price, value, util_value, util_class):
        '''DEFAULT CONSTRUCTOR'''
        super(GiftUtility, self).__init__(price, value)
        self.type = 'Utility'
        self.util_value = util_value
        self.util_class = util_class
