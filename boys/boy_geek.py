'''GEEK BOY'''

import boy as base

class BoyGeek(base.Boy):

    '''DEFAULT CONSTRUCTOR'''
    def __init__(self, name, attr, budget, intel):
        super(BoyGeek, self).__init__(name, attr, budget, intel)
