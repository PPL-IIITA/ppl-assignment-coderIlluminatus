'''BOY'''

class Boy(object):

    '''BASE CLASS'''

    def __init__(self, name, attr, budget, intel, min_attr):
        '''DEFAULT CONSTRUCTOR'''
        self.name = name
        self.attr = attr
        self.budget = budget
        self.intel = intel
        self.min_attr = min_attr
        self.status = 'Single'
        self.partner = None
        self.happiness = 0

    def check_elligibility(self, girl):
        '''CHECKS WHETHER THIS BOY IS ELIGIBLE FOR PAIRING WITH THE CURRENT GIRL'''
        if (self.budget >= girl.mcost) and (girl.attr >= self.min_attr):
            return True
        return False

    def match(self, girl):
        '''ASSIGNS GIRL AS THE PARTNER FOR THIS BOY'''
        self.status = 'Committed'
        self.partner = girl

    def break_up(self):
        '''BREAKS UP WITH CURRENT PARTNER'''
        self.status = 'Single'
        self.partner = None

    def get_primary_attribute(self):
        '''RETURNS PRIMARY CRITERION ATTRIBUTE'''
        return self.budget
