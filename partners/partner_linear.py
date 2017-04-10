'''LIST IMPLEMENTATION OF PARTNER'''

from partners.partner import Partner

class PartnerLinear(Partner):

    '''USES INHERITANCE'''

    def __init__(self, boy_name_list):
        '''DEFAULT CONSTRUCTOR'''
        super(PartnerLinear, self).__init__(boy_name_list)

    def get_girlfriend_name_linear_search(self):
        '''RETURNS GIRLFRIEND NAME LIST USING LIST IMPLEMENTATION'''
        super(PartnerLinear, self).generate_committed_boy_pool()
        for boy_name in self.boy_name_list:
            has_girlfriend = False
            for boy in self.committed_boy_pool:
                if boy.name == boy_name:
                    has_girlfriend = True
                    self.girl_name_list.append(boy.partner.name)
            if not has_girlfriend:
                self.girl_name_list.append('NO GIRLFRIEND')
        return self.girl_name_list
