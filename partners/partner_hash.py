'''HASH TABLE IMPLEMENTATION OF PARTNER'''

from partners.partner import Partner

class PartnerHash(Partner):

    '''USES INHERITANCE'''

    def __init__(self, boy_name_list):
        '''DEFAULT CONSTRUCTOR'''
        self.boy_hash = {}
        super(PartnerHash, self).__init__(boy_name_list)

    def generate_boy_hash(self):
        '''GENERATES HASH TABLE OF BOY NAMES AND THEIR CORRESPONDING GIRLFRIEND NAMES'''
        super(PartnerHash, self).generate_committed_boy_pool()
        for boy in self.committed_boy_pool:
            self.boy_hash[boy.name] = boy.partner.name

    def get_girlfriend_name_hash_table(self):
        '''RETURNS GIRLFRIEND NAME LIST USING HASH TABLE IMPLEMENTATION'''
        self.generate_boy_hash()
        for boy_name in self.boy_name_list:
            self.girl_name_list.append(self.boy_hash[boy_name])
        return self.girl_name_list
