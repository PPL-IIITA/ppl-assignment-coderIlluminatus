'''SELECTS AT LEAST ONE GIFT OF EVERY TYPE'''

import logging
from selectors.selector import Selector
from gifts.gift_essential import GiftEssential
from gifts.gift_utility import GiftUtility
from gifts.gift_luxury import GiftLuxury

class SelectorEvery(Selector):

    '''USES INHERITANCE'''

    def __init__(self, couple, gifts_list):
        '''DEFAULT CONSTRUCTOR'''
        super(SelectorEvery, self).__init__(couple, gifts_list)

    def select_gifts(self):
        '''SELECTS GIFTS FOR A PARTICULAR COUPLE'''
        super(SelectorEvery, self).select_gifts()
        flag_essential, flag_utility, flag_luxury = False, False, False
        for gift in self.couple.gift_basket:
            if isinstance(gift, GiftEssential):
                flag_essential = True
            elif isinstance(gift, GiftUtility):
                flag_utility = True
            else:
                flag_luxury = True

        if not flag_essential:
            for gift in self.gifts_list:
                if isinstance(gift, GiftEssential):
                    self.give_additional(gift)
                    break

        if not flag_utility:
            for gift in self.gifts_list:
                if isinstance(gift, GiftUtility):
                    self.give_additional(gift)
                    break

        if not flag_luxury:
            for gift in self.gifts_list:
                if isinstance(gift, GiftLuxury):
                    self.give_additional(gift)
                    break

    def give_additional(self, gift):
        '''ADDS AN ADDITONAL GIFT TO THE COUPLE'S GIFT BASKET'''
        logging.info('GIFTING   :\t' + self.couple.boy.name + ' is giving ' + gift.name + ' to ' + self.couple.girl.name + ' (ADDITIONAL)')
        self.couple.gift_basket.append(gift)
