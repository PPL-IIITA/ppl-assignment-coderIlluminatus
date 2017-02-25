'''GIRL'''

class Girl(object):

    '''BASE CLASS'''

    def __init__(self, name, attr, mcost, intel, nature, criteria):
        self.name = name
        self.attr = attr
        self.mcost = mcost
        self.intel = intel
        self.status = 'Single'
        self.nature = nature
        self.partner = None
        self.happiness = 0
        self.criteria = criteria

    def check_elligibility(self, boy):
        '''CHECKS WHETHER THIS BOY IS ELIGIBLE FOR PAIRING WITH THE CURRENT GIRL'''
        if self.mcost <= boy.budget:
            return True
        return False

    def match(self, boy):
        '''ASSIGNS BOY AS THE PARTNER FOR THIS GIRL'''
        self.status = 'Committed'
        self.partner = boy