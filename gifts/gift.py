'''GIFT'''

class Gift(object):

    '''BASE CLASS'''

    def __init__(self, name, price, value):
        '''DEFAULT CONSTRUCTOR'''
        self.name = name
        self.price = price
        self.value = value

    def get_primary_attribute(self):
        '''RETURNS PRIMARY CRITERION ATTRIBUTE'''
        return -self.price
