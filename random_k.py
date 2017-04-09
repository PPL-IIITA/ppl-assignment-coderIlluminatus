'''A DATA STRUCTURE TO GENERATE RANDOM k ITEMS IN A LIST'''

from random import shuffle

class TopK(object):

    '''RANDOM k CLASS FOR THE DATA STRUCTURE'''

    def __init__(self, generic_list):
        '''DEFAULT CONSTRUCTOR'''
        self.generic_list = generic_list

    def get_top_k(self, k):
        '''YIELDS RANDOM k RESULTS'''
        shuffle(self.generic_list)
        return self.generic_list[:k]
