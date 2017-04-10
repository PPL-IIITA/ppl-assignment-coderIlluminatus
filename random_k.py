'''A DATA STRUCTURE TO GENERATE RANDOM OUT OF BEST n ITEMS IN A LIST'''

from random import randint

class RandomK(object):

    '''RANDOM k CLASS FOR THE DATA STRUCTURE'''

    def __init__(self, generic_list):
        '''DEFAULT CONSTRUCTOR'''
        self.generic_list = sorted(generic_list, key=lambda x: x.get_primary_attribute(), reverse=True)

    def get_random_k(self, n):
        '''YIELDS RANDOM RESULT OUT OF BEST n ELEMENTS'''
        k = randint(0, min(n, len(self.generic_list)))
        sliced_list = self.generic_list[:n]
        return sliced_list[k - 1]
