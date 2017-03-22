'''ESSENTIAL GIFT'''

from gifts.gift import Gift

class GiftEssential(Gift):

    '''DEFAULT CONSTRUCTOR'''
    def __init__(self, name, price, value):
        super(GiftEssential, self).__init__(name, price, value)
