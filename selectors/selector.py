'''SELECTOR'''

import sys
sys.path.append("..")

from algorithms import select_gifts

class Selector(object):

    '''BASE CLASS'''

    def __init__(self, couple, gifts_list):
        '''DEFAULT CONSTRUCTOR'''
        self.couple = couple
        self.gifts_list = gifts_list

    def select_gifts(self):
        '''SELECTS GIFTS FOR A PARTICULAR COUPLE'''
        select_gifts(self.couple, self.gifts_list)
