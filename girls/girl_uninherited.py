'''GIRL'''

class Girl(object):

    '''DOES NOT USE INHERITANCE'''

    def __init__(self, name, attr, mcost, intel, nature):
        self.name = name
        self.attr = attr
        self.mcost = mcost
        self.intel = intel
        self.status = 'Single'
        self.nature = nature
        self.partner = ''
        self.happiness = 0

    def check_elligibility(self, boy):
        '''CHECKS WHETHER THIS BOY IS ELIGIBLE FOR PAIRING WITH THE CURRENT GIRL'''
        if self.mcost <= boy.budget:
            return True
        return False
