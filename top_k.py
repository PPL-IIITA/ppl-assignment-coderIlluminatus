'''A DATA STRUCTURE TO GENERATE TOP k ITEMS IN A LIST'''

class TopK(object):

    '''TOP k CLASS FOR THE DATA STRUCTURE'''

    def __init__(self, generic_list):
        '''DEFAULT CONSTRUCTOR'''
        self.generic_list = sorted(generic_list, key=lambda x: x.get_primary_attribute(), reverse=True)

    def get_top_k(self, k):
        '''YIELDS TOP k RESULTS'''
        return self.generic_list[:k]
