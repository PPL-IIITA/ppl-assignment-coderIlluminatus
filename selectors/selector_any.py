'''SELECTS GIFTS OF ANY TYPE'''

from selectors.selector import Selector

class SelectorAny(Selector):

    '''USES INHERITANCE'''

    def __init__(self, couple, gifts_list):
        '''DEFAULT CONSTRUCTOR'''
        super(SelectorAny, self).__init__(couple, gifts_list)

    def select_gifts(self):
        '''SELECTS GIFTS FOR A PARTICULAR COUPLE'''
        super(SelectorAny, self).select_gifts()
