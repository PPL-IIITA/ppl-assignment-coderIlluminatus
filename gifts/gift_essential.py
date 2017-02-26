'''ESSENTIAL GIFT'''

import gift as base

class GiftEssential(base.Gift):

    '''DEFAULT CONSTRUCTOR'''
    def __init__(self, price, value):
        super(GiftEssential, self).__init__(price, value)
        self.type = 'Essential'
