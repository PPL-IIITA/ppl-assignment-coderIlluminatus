'''GIFT'''

class Gift(object):

    '''DOES NOT USE INHERITANCE'''

    def __init__(self, name, price, value, nature, rating, difficulty, util_value, util_class):
        '''DEFAULT CONSTRUCTOR'''
        self.name = name
        self.price = price
        self.value = value
        self.nature = nature

        #EXTRA ATTRIBUTES FOR LUXURY GIFT
        self.rating = rating
        self.difficulty = difficulty

        #EXTRA ATTRIBUTES FOR UTILITY GIFT
        self.util_value = util_value
        self.util_class = util_class
