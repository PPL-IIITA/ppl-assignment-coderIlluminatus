'''A DATA STRUCTURE TO GENERATE RANDOM OUT OF BEST k ITEMS IN A LIST'''

from random import randint

class TopK(object):

    '''RANDOM k CLASS FOR THE DATA STRUCTURE'''

    def __init__(self, generic_list):
        '''DEFAULT CONSTRUCTOR'''
        sself.generic_list = sorted(generic_list, key=lambda x: x.get_primary_attribute(), reverse=True)

    def get_top_k(self, k):
        '''YIELDS RANDOM k RESULTS'''
        
        return self.generic_list[:k][]
