'''BOY'''

class Boy(object):

    '''DOES NOT USE INHERITANCE'''

    def __init__(self, name, attr, budget, intel, min_attr, nature):
        '''DEFAULT CONSTRUCTOR'''
        self.name = name
        self.attr = attr
        self.budget = budget
        self.intel = intel
        self.min_attr = min_attr
        self.status = 'Single'
        self.nature = nature
        self.partner = ''
        self.happiness = 0

    def check_elligibility(self, girl):
        '''CHECKS WHETHER THIS BOY IS ELIGIBLE FOR PAIRING WITH THE CURRENT GIRL'''
        if (self.budget >= girl.mcost) and (girl.attr >= self.min_attr):
            return True
        return False
